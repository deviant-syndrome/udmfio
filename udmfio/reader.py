from collections import defaultdict
from os import PathLike
from typing import Dict
from typing import Union, Any, List

from .specs.linedef import Linedef
from .specs.sector import Sector
from .specs.sidedef import Sidedef
from .specs.thing import Thing
from .specs.udmf_map import UDMFMap
from .specs.vertex import Vertex
from .parser import parse_udmf, UDMFOutputType


def create_udmf_map(parser_output: UDMFOutputType) -> UDMFMap:
    """
    Converts the parser output into a structured UDMF map representation.

    Args:
        parser_output (UDMFOutputType): A list of tuples where each tuple represents a UDMF block.
        The first element of the tuple is the block name (e.g., "thing") and the second element is a list of key-value
        pairs representing the block's attributes.

    Returns:
        UDMFMap: An object representing the UDMF map containing lists of each UDMF block type.

    Example:
        Given a parser output:
        ```
        [('thing', [('id', 1), ('type', 3004), ('x', -64.0), ('y', 64.0), ('angle', 90)])]
        ```

        This function will populate an instance of the UDMFMap class with instances of Thing, Linedef, etc.

    Raises:
        TypeError: If any block type does not match the expected properties.
    """

    udmf_map = UDMFMap()
    property_dict: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    udmf_map.namespace = property_dict['namespace']

    for token_type, properties in parser_output:
        # Append the properties dictionary to the list for the given token_type
        property_dict[token_type].append({prop: value for prop, value in properties})

    linedef_blocks = property_dict['linedef']
    for linedef_properties in linedef_blocks:
        # Create instances of your classes or perform processing
        linedef_instance = Linedef(**linedef_properties)
        udmf_map.linedefs.append(linedef_instance)

    vertex_blocks = property_dict['vertex']
    for vertex_properties in vertex_blocks:
        # Create instances of your classes or perform processing
        vertex_instance = Vertex(**vertex_properties)
        udmf_map.vertexes.append(vertex_instance)

    sidedef_blocks = property_dict['sidedef']
    for sidedef_properties in sidedef_blocks:
        # Create instances of your classes or perform processing
        sidedef_instance = Sidedef(**sidedef_properties)
        udmf_map.sidedefs.append(sidedef_instance)

    sector_blocks = property_dict['sector']
    for sector_properties in sector_blocks:
        # Create instances of your classes or perform processing
        sector_instance = Sector(**sector_properties)
        udmf_map.sectors.append(sector_instance)

    thing_blocks = property_dict['thing']
    for thing_properties in thing_blocks:
        # Create instances of your classes or perform processing
        thing_instance = Thing(**thing_properties)
        udmf_map.things.append(thing_instance)

    return udmf_map


def load_udmf_map(file_path: Union[str, bytes, PathLike]) -> UDMFMap:
    """
    Loads a UDMF map from the provided file path.

    Args:
        file_path (Union[str, bytes, PathLike]): The path to the UDMF file.

    Returns:
        UDMFMap: An object representing the UDMF map with structured data.

    Example:
        Given a UDMF file located at 'path/to/udmf.txt',
        calling `load_udmf_map('path/to/udmf.txt')` will return a structured UDMFMap object.

    Raises:
        FileNotFoundError: If the UDMF file is not found at the provided path.
        SyntaxError: If the file content does not conform to the UDMF syntax.
    """
    parser_output: UDMFOutputType = parse_udmf(file_path)
    udmf_map: UDMFMap = create_udmf_map(parser_output)
    return udmf_map
