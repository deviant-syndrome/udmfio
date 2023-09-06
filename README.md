# UDMFIO UDMF Map Parser and Writer

## Overview
This project provides utilities to parse and generate Universal Doom Map Format (UDMF) maps. UDMF is a human-readable representation of map data, widely recognized in modern DOOM mapping.
The parsing of UDMF file is done using PLY parser, build according to the official [UDMF specification](https://github.com/ZDoom/gzdoom/blob/master/specs/udmf.txt). 
The binding of parsed data to Python classes is done for specification-standardised fields and [ZDoom extensions](https://github.com/ZDoom/gzdoom/blob/master/specs/udmf_zdoom.txt). 

## Features

- **Parsing UDMF Maps**: Quickly turn UDMF-formatted text into a structured representation using the `parse_udmf` function.

- **Writing UDMF Maps**: Convert structured map data back into the UDMF text format for use in map editors or game engines.

- **Customizable bindings**: The parser and writer are built in a way that lets you easily adapt or extend them for specific needs.

## Usage

### Parsing
```python
from udmf_parser import parse_udmf

parsed_data = parse_udmf("TEXTMAP.lmp")
print(parsed_data)
```

### Writing to file
```python
from udmf_writer import write_udmf_map

write_udmf_map(parsed_data, "path_to_output_file.txt")
```

### Customizing
The core functionality is built using classes and mixins, allowing for easy customization or extension. For instance, the UDMFMixin class provides a convenient way to convert any object to its UDMF string representation. Check out classes like UDMFLinedef, UDMFSidedef, etc., to see how this can be applied to specific DOOM map structures.

### Testing
Extensive unit tests are provided to ensure the correct behavior of both the parser and the writer. To run the test
```bash
python -m unittest discover -s tests
```

### License
0BSD