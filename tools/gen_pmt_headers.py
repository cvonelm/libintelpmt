import sys
import re
import os

from lxml import etree
import jinja2

dirname = os.path.dirname(__file__)
xmlparser = etree.XMLParser(
    ns_clean=True, remove_comments=True, remove_blank_text=True, resolve_entities=False
)

# sample: name, offset, size
# transformer name, function
# interface name, function, inputs = []


# the XML uses **, which is not C++, use pow instead
def replace_pow_operator(text):
    m = re.match(r"(.*)([0-9_$a-z]+)\s*\*\*\s*([0-9_$a-z]+)(.*)", text)
    if m:
        return m.group(1) + "pow(" + m.group(2) + "," + m.group(3) + ")" + m.group(4)
    return text


# cant have . in c++ function names
def normalize_trans_name(text):
    return text.replace(".", "DOT")


# remove leading 0x, use all lower hex
def normalize_uniqueid(uniqueid):
    if uniqueid.startswith("0x"):
        uniqueid = uniqueid[2:]
    return uniqueid.lower()


def normalize_counter_name(name):
    # fudging spaces in counternames, really?
    return name.replace(" ", "")


def normalize_counter_type(name):
    name = name.replace("[", "_")
    name = name.replace("]", "_")
    return name.replace(" ", "_")


def parse_aggr_interface(filename):
    transformations = []
    aggregators = []
    aggr_interface_filename = filename[:-4] + "_interface.xml"
    aggr_interface = etree.parse(aggr_interface_filename, xmlparser).getroot()
    for elem in aggr_interface.iter("{*}TransFormation"):
        trans_func = replace_pow_operator(elem.find("{*}transform").text)
        trans_func = trans_func.replace("$param", "param")
        transformation = {}
        transformation['type'] = elem.find("{*}output_dataclass").text
        transformation["name"] = normalize_trans_name(elem.attrib["transformID"])
        transformation["function"] = trans_func

        if "parameter_1" in transformation["function"]:
            transformation["twoargs"] = True
        else:
            transformation["twoargs"] = False
        transformations.append(transformation)
    for elem in aggr_interface.iter("{*}T_AggregatorSample"):
        name = (
            normalize_counter_name(elem.attrib["sampleGroup"])
            + "::"
            + elem.attrib["sampleName"]
        )
        counter_type = normalize_counter_type(
            normalize_counter_name(elem.attrib["sampleGroup"])
            + "_"
            + elem.attrib["sampleName"]
        )
        # Counters that contain "reserved" are reserved for future use. They give
        # you headaches as their names repeat and they read 0 always anyways, so
        # skip em
        if "reserved" in name.lower():
            continue
        inputs = []
        for input in elem.iter("{*}TransFormInput"):
            input_group = input.find("{*}sampleGroupIDREF").text
            input_id = input.find("{*}sampleIDREF").text
            inputs.append(normalize_counter_type(input_group + "_" + input_id))
        trans_func = normalize_trans_name(elem.find("{*}transformREF").text)
        aggregators.append(
            {
                "name": name,
                "type": counter_type,
                "function": trans_func,
                "inputs": inputs,
            }
        )
    return [transformations, aggregators]


if len(sys.argv) != 3:
    print("Usage: gen_pmt_headers.py [path to Intel-PMT repo] [destination]")
    exit(-1)

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

aggregator_files = []
for root, subdirs, files in os.walk(os.path.join(source_dir, "xml")):
    for file in files:
        if file.endswith("aggregator.xml"):
            aggregator_files.append(os.path.join(root, file))


templateLoader = jinja2.FileSystemLoader(dirname + "/templates")
templateEnv = jinja2.Environment(
    loader=templateLoader, trim_blocks=True, lstrip_blocks=True
)
header_template = templateEnv.get_template("pmt_definition.hpp.jinja")
cpp_template = templateEnv.get_template("pmt_definition.cpp.jinja")
union_header_template = templateEnv.get_template("libintelpmt.hpp.jinja")

os.makedirs(dest_dir + "/include/libintelpmt", exist_ok=True)
os.makedirs(dest_dir + "/src", exist_ok=True)

uniqueids = []
for file in aggregator_files:
    transformations, aggregators = parse_aggr_interface(file)
    outer_size = 0
    pmt_device = {}
    aggregator = etree.parse(file, xmlparser).getroot()
    uniqueid = normalize_uniqueid(aggregator.find("{*}uniqueid").text)
    uniqueids.append(uniqueid)
    samples = []
    for sample_group in aggregator.iter("{*}SampleGroup"):
        sample_group_name = sample_group.attrib["sampleGroupID"]
        for sample in sample_group.iter("{*}sample"):
            sample_name = sample.attrib["sampleID"]
            sample_info = {}
            sample_info["name"] = normalize_counter_type(
                sample_group_name + "_" + sample_name
            )
            sample_info["offset"] = outer_size + int(sample.find("{*}lsb").text)
            sample_info["size"] = int(sample.find("{*}size").text)
            samples.append(sample_info)
        outer_size = outer_size + int(sample_group.find("{*}length").text)
    header_template.stream(
        uniqueid=uniqueid,
        transformations=transformations,
        aggregators=aggregators,
        samples=samples,
    ).dump(dest_dir + "/include/libintelpmt/pmt_" + uniqueid + ".hpp")
    cpp_template.stream(
        uniqueid=uniqueid,
        transformations=transformations,
        aggregators=aggregators,
        samples=samples,
    ).dump(dest_dir + "/src/pmt_" + uniqueid + ".cpp")

union_header_template.stream(uniqueids=uniqueids).dump(dest_dir + "/include/libintelpmt/libintelpmt.hpp")
