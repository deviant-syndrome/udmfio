from udmfio import UDMFMap

from .specs.linedef import Linedef
from .specs.sector import Sector
from .specs.sidedef import Sidedef
from .specs.thing import Thing
from .specs.vertex import Vertex


class UDMFMixin:
    """
    A mixin class to support the conversion of objects to UDMF (Universal Doom Map Format) string representation.

    This mixin assumes that the object's attributes (stored in its `__dict__`) need to be represented in
    the UDMF string format.
    """

    @staticmethod
    def _dict_to_udmf_string(dictionary: dict, name: str) -> str:
        """
        Convert a dictionary to a UDMF formatted string.

        Args:
            dictionary (dict): A dictionary of properties to be represented in UDMF format.
            name (str): The name to be used as the block's name in the UDMF string.

        Returns:
            str: The UDMF formatted string representation of the provided dictionary.

        Notes:
            - Keys with value as None or with the name 'kwargs' are ignored.
            - Boolean values are represented in lowercase (e.g., true/false).
            - Int and float values are represented as they are.
            - Other types of values are represented as quoted strings.
        """
        udmf_string = '{}\n{{\n'.format(name)
        for key, value in dictionary.items():
            if value is None or key == 'kwargs':
                continue
            if isinstance(value, bool):
                udmf_string += '  {}={};\n'.format(key, str(value).lower())
            elif isinstance(value, (int, float)):
                udmf_string += '  {}={};\n'.format(key, value)
            else:
                udmf_string += '  {}="{}";\n'.format(key, value)
        udmf_string += '}\n'
        return udmf_string

    def to_udmf_string(self) -> str:
        """
        Convert the object to a UDMF formatted string.

        This method utilizes the object's attributes stored in its `__dict__` to generate the UDMF string.

        Returns:
            str: The UDMF formatted string representation of the object.
        """
        return self._dict_to_udmf_string(self.__dict__, self.__class__.__bases__[0].__name__.lower())


class UDMFLinedef(Linedef, UDMFMixin):
    def __init__(self, original):
        # Copy attributes from the original instance
        super().__init__()
        for attr, value in original.__dict__.items():
            setattr(self, attr, value)


class UDMFSidedef(Sidedef, UDMFMixin):
    def __init__(self, original):
        # Copy attributes from the original instance
        super().__init__()
        for attr, value in original.__dict__.items():
            setattr(self, attr, value)


class UDMFSector(Sector, UDMFMixin):
    def __init__(self, original):
        # Copy attributes from the original instance
        super().__init__()
        for attr, value in original.__dict__.items():
            setattr(self, attr, value)


class UDMFVertex(Vertex, UDMFMixin):
    def __init__(self, original):
        # Copy attributes from the original instance
        super().__init__()
        for attr, value in original.__dict__.items():
            setattr(self, attr, value)


# Thing
class UDMFThing(Thing, UDMFMixin):
    def __init__(self, original):
        # Copy attributes from the original instance
        super().__init__()
        for attr, value in original.__dict__.items():
            setattr(self, attr, value)


def write_udmf_map(udmf_map: UDMFMap, file_path: str) -> None:
    """
    Writes the UDMFMap object to a file in the UDMF format.

    Args:
        udmf_map (UDMFMap): An instance of the UDMFMap class, representing a UDMF map.
        file_path (str): The path to the file where the UDMF map should be written.

    Note:
        This function will overwrite the contents of the file if it already exists.

    Example:
        Given an UDMFMap instance with linedefs, sidedefs, sectors, vertices, and things,
        it writes each component's UDMF representation to the specified file.
    """
    with open(file_path, 'w') as f:
        # Writing Linedefs
        for linedef in udmf_map.linedefs:
            udmf_linedef = UDMFLinedef(linedef)
            f.write(udmf_linedef.to_udmf_string())

        # Writing Sidedefs
        for sidedef in udmf_map.sidedefs:
            udmf_sidedef = UDMFSidedef(sidedef)
            f.write(udmf_sidedef.to_udmf_string())

        # Writing Sectors
        for sector in udmf_map.sectors:
            udmf_sector = UDMFSector(sector)
            f.write(udmf_sector.to_udmf_string())

        # Writing Vertices
        for vertex in udmf_map.vertexes:
            udmf_vertex = UDMFVertex(vertex)
            f.write(udmf_vertex.to_udmf_string())

        # Writing Things
        for thing in udmf_map.things:
            udmf_thing = UDMFThing(thing)
            f.write(udmf_thing.to_udmf_string())
