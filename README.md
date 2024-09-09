# libintelpmt - C++ library for reading intel_pmt counters

This is a C++ library which can be used to parse the data coming from intel_pmt.
It accomplishes this task by translating Intel's XML descriptions to C++ files.

For a description of the API see: API.md.

This library is licensed under the terms of the MIT license, for more information see LICENSE.

## Requirements

- For the generation of the PMT files:
    - Python 3
    - lxml, to parse the XML files
    - jinja2, to generate the hpp/cpp files
- C++17 compatible compiler


