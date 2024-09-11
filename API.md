# API Documentation

## Overview

libintelpmt uses the XML files supplied by Intel describing the counters contained in the
different types of PMT devices to generate C++ files to be able to read them.


libintelpmt differentiates between `Sample`s and `Counter`s.

A `Sample` is a raw value as it can be obtained directly from the PMT memory by reading it at the correct offset with not further processing.

A `Counter` is a processed combination of one or more `Sample`s according to the rules
laid down in the Intel PMT XML files.

libintelpmt splits the job of reading counters into two classes:
`Device` and `DeviceInstance`.

`Device` records information about a PMT_Device, such as the uniqueid, its path in the sysfs, contained counters. The different PMT devices exist as specializations of the generic `EDevice` class.

`DeviceInstance` represents a PMT Device "in-flight". To be able to read data from a `Devicve` a `DeviceInstance` is opened from a `Device`. `DeviceInstance` uses `mmap()` internally to access the file.

## General interfaces

### std::vector<intelpmt::Device>  intelpmt::get_pmt_devices()

Returns a list of the PMT devices found in `/sys/class/intel_pmt` for which information is
present in lbintelpmt. Devices which are not found in libintelpmt will be skipped.

## struct Unit

A struct describing a unit. Contains a string field `unit`, which either contains a unit, `#` if no unit was specified or `enum` if the unit is an enum.
If the `unit` is `enum`, then there is a second field `print_function` which contains a function that translates the counter value to a string representation
of the enumeration value.

## class Device

`Device` a `DeviceInstance` is opened from a `Device`. `DeviceInstance` uses `mmap()` internally to access the file.

### DeviceInstance open()

Opens a new `DeviceInstance` from the `Device`.

### const std::map<uint64_t struct Unit> get_units()

Returns a mapping from counter to unit.

### const std::map<std::string, uint64_t>& get_counter_names()

Returns a mapping of the names of the counters to their counter id.

### const std::map<uint64_t, struct Sample>&  get_samples()

Returns a mapping from `Sample` IDs to the `struct Sample` describing the size and offset of the value.

### const std::map<uint64_t, struct Counter>& get_counters()

Returns a mapping from Counter ID to the `struct Counter` describing how it is computed from a set of `Sample`s.

### const std::filesystem::path get_path()

Returns the sysfs-Path of the PMT Device.

### const uint64_t  get_uniqueid()

Returns the uniqueid of the PMT Device.

## DeviceInstance


### const& Device get_device()

Returns the Device from which this DeviceInstance was opened.

### double read_counter(uint64_t counter_id)

Reads the counter specified by `counter_id`.

### uint64_t read_sample(uint64_t event)

Reads the sample specified by `event`.
