predefined = {}


predefined['b15a0edd']  = {}
predefined['b15a0edd']['aggregators'] = [
     { "name" : "HBM0MaxDeviceTemperature", "type" : "HBM0MaxDeviceTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "HBM0MaxDeviceTemperature" ] },
      { "name" : "HBM1MaxDeviceTemperature", "type" : "HBM1MaxDeviceTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "HBM1MaxDeviceTemperature" ] },
      { "name" : "TileMinTemperature", "type" : "TileMinTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "TileMinTemperature" ] },
      { "name" : "TileMaxTemperature", "type" : "TileMaxTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "TileMaxTemperature" ] },
      { "name" : "GTMinTemperature", "type" : "GTMinTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "GTMinTemperature" ] },
      { "name" : "GTMaxTemperature", "type" : "GTMaxTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "GTMaxTemperature" ] },
      { "name" : "VF0_VFID", "type" : "VF0_VFID", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_VFID" ] },
      { "name" : "VF0_HBM0_READ", "type" : "VF0_HBM0_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM0_READ" ] },
      { "name" : "VF0_HBM0_WRITE", "type" : "VF0_HBM0_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM0_WRITE" ] },
      { "name" : "VF0_HBM1_READ", "type" : "VF0_HBM1_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM1_READ" ] },
      { "name" : "VF0_HBM1_WRITE", "type" : "VF0_HBM1_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM1_WRITE" ] },
      { "name" : "VF0_TIMESTAMP", "type" : "VF0_TIMESTAMP", "datatype" : "scalar", "function" : "u64", "inputs" : [ "VF0_TIMESTAMP_H",  "VF0_TIMESTAMP_L" ] },
      { "name" : "VF1_VFID", "type" : "VF1_VFID", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_VFID" ] },
      { "name" : "VF1_HBM0_READ", "type" : "VF1_HBM0_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM0_READ" ] },
      { "name" : "VF1_HBM0_WRITE", "type" : "VF1_HBM0_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM0_WRITE" ] },
      { "name" : "VF1_HBM1_READ", "type" : "VF1_HBM1_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM1_READ" ] },
      { "name" : "VF1_HBM1_WRITE", "type" : "VF1_HBM1_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM1_WRITE" ] },
      { "name" : "VF1_TIMESTAMP", "type" : "VF1_TIMESTAMP", "datatype" : "scalar", "function" : "u64", "inputs" : [ "VF1_TIMESTAMP_H", "VF1_TIMESTAMP_L" ] },
      { "name" : "HBM2MaxDeviceTemperature", "type" : "HBM2MaxDeviceTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "HBM2MaxDeviceTemperature" ] },
      { "name" : "HBM3MaxDeviceTemperature", "type" : "HBM3MaxDeviceTemperature", "datatype" : "scalar", "function" : "u32", "inputs" : [ "HBM3MaxDeviceTemperature" ] },
      { "name" : "VF0_HBM2_READ", "type" : "VF0_HBM2_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM2_READ" ] },
      { "name" : "VF0_HBM2_WRITE", "type" : "VF0_HBM2_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM2_WRITE" ] },
      { "name" : "VF0_HBM3_READ", "type" : "VF0_HBM3_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM3_READ" ] },
      { "name" : "VF0_HBM3_WRITE", "type" : "VF0_HBM3_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF0_HBM3_WRITE" ] },
      { "name" : "VF1_HBM2_READ", "type" : "VF1_HBM2_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM2_READ" ] },
      { "name" : "VF1_HBM2_WRITE", "type" : "VF1_HBM2_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM2_WRITE" ] },
      { "name" : "VF1_HBM3_READ", "type" : "VF1_HBM3_READ", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM3_READ" ] },
      { "name" : "VF1_HBM3_WRITE", "type" : "VF1_HBM3_WRITE", "datatype" : "scalar", "function" : "u32", "inputs" : [ "VF1_HBM3_WRITE" ] }
]

predefined['b15a0edd']['datatypes'] = {
        'scalar' : {'type' : "scalar", "unit" : "#" }
    }

predefined['b15a0edd']['transformations'] = [
        {"type" : "float", "name" : "u32", "function" : "parameter_0", "twoargs" : False},
        {"type" : "float", "name" : "u64", "function" : "(parameter_1 << 32) | parameter_0", "twoargs" : True}
]


predefined['b15a0edd']['samples'] = [ 
     { "name" : "HBM0MaxDeviceTemperature", "offset" : 28 * 8, "size" : 32 },
      { "name" : "HBM1MaxDeviceTemperature", "offset" : 36 * 8, "size" : 32 },
      { "name" : "TileMinTemperature", "offset" : 40 * 8, "size" : 32 },
      { "name" : "TileMaxTemperature", "offset" : 44 * 8, "size" : 32 },
      { "name" : "GTMinTemperature", "offset" : 48 * 8, "size" : 32 },
      { "name" : "GTMaxTemperature", "offset" : 52 * 8, "size" : 32 },
      { "name" : "VF0_VFID", "offset" : 88 * 8, "size" : 32 },
      { "name" : "VF0_HBM0_READ", "offset" : 92 * 8, "size" : 32 },
      { "name" : "VF0_HBM0_WRITE", "offset" : 96 * 8, "size" : 32 },
      { "name" : "VF0_HBM1_READ", "offset" : 104 * 8, "size" : 32 },
      { "name" : "VF0_HBM1_WRITE", "offset" : 108 * 8, "size" : 32 },
      { "name" : "VF0_TIMESTAMP_L", "offset" : 168 * 8, "size" : 32 },
      { "name" : "VF0_TIMESTAMP_H", "offset" : 172 * 8, "size" : 32 },
      { "name" : "VF1_VFID", "offset" : 176 * 8, "size" : 32 },
      { "name" : "VF1_HBM0_READ", "offset" : 180 * 8, "size" : 32 },
      { "name" : "VF1_HBM0_WRITE", "offset" : 184 * 8, "size" : 32 },
      { "name" : "VF1_HBM1_READ", "offset" : 192 * 8, "size" : 32 },
      { "name" : "VF1_HBM1_WRITE", "offset" : 196 * 8, "size" : 32 },
      { "name" : "VF1_TIMESTAMP_L", "offset" : 256 * 8, "size" : 32 },
      { "name" : "VF1_TIMESTAMP_H", "offset" : 260 * 8, "size" : 32 },
      { "name" : "HBM2MaxDeviceTemperature", "offset" : 300 * 8, "size" : 32 },
      { "name" : "HBM3MaxDeviceTemperature", "offset" : 308 * 8, "size" : 32 },
      { "name" : "VF0_HBM2_READ", "offset" : 312 * 8, "size" : 32 },
      { "name" : "VF0_HBM2_WRITE", "offset" : 316 * 8, "size" : 32 },
      { "name" : "VF0_HBM3_READ", "offset" : 328 * 8, "size" : 32 },
      { "name" : "VF0_HBM3_WRITE", "offset" : 332 * 8, "size" : 32 },
      { "name" : "VF1_HBM2_READ", "offset" : 344 * 8, "size" : 32 },
      { "name" : "VF1_HBM2_WRITE", "offset" : 348 * 8, "size" : 32 },
      { "name" : "VF1_HBM3_READ", "offset" : 360 * 8, "size" : 32 },
      { "name" : "VF1_HBM3_WRITE", "offset" : 364 * 8, "size" : 32 },
        ]

predefined["41fe79a5"] = {}

predefined["41fe79a5"]['samples'] = [
        { "name" : "PPIN", "offset" : 72 * 8, "size" : 32}
        ]

predefined['41fe79a5']['datatypes'] = {
        'scalar' : {'type' : "scalar", "unit" : "#" }
    }

predefined['41fe79a5']['transformations'] = [
        {"type" : "float", "name" : "u32", "function" : "parameter_0", "twoargs" : False},
        {"type" : "float", "name" : "u64", "function" : "(parameter_1 << 32) | parameter_0", "twoargs" : True}
]

predefined['41fe79a5']['aggregators'] = [
        { "name" : "PPIN", "type" : "PPIN", "datatype" : "scalar", "function" : "u32", "inputs" : [ "PPIN" ] }
        ]
