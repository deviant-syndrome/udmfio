import unittest

from udmfio import Thing, Sector, Linedef, Vertex, Sidedef
from udmfio.reader import create_udmf_map


class TestCreateUDMFMap(unittest.TestCase):

    def setUp(self):
        # This will run before each test
        self.parser_output = [
            ('thing', [('type', 3004), ('x', -64.0), ('y', 64.0), ('angle', 90)]),
            ('linedef', [('v1', 1), ('v2', 2)]),
            ('vertex', [('x', 10.0), ('y', -5.0)]),
            ('sidedef', [('texturemiddle', 'STARTAN3'), ('sector', 1)]),
            ('sector', [('texturefloor', 'FLOOR4_8'), ('textureceiling', 'CEIL3_5')])
        ]

    def test_create_udmf_map(self):
        udmf_map = create_udmf_map(self.parser_output)

        # Verifying the Thing object
        self.assertIsInstance(udmf_map.things[0], Thing)
        self.assertEqual(udmf_map.things[0].type, 3004)

        # Verifying the Linedef object
        self.assertIsInstance(udmf_map.linedefs[0], Linedef)
        self.assertEqual(udmf_map.linedefs[0].v1, 1)

        # Verifying the Vertex object
        self.assertIsInstance(udmf_map.vertexes[0], Vertex)
        self.assertEqual(udmf_map.vertexes[0].y, -5)

        # Verifying the Sidedef object
        self.assertIsInstance(udmf_map.sidedefs[0], Sidedef)
        self.assertEqual(udmf_map.sidedefs[0].sector, 1)

        # Verifying the Sector object
        self.assertIsInstance(udmf_map.sectors[0], Sector)
        self.assertEqual(udmf_map.sectors[0].texturefloor, "FLOOR4_8")

    def test_invalid_parser_output(self):
        invalid_parser_output = [
            ('linedef', [("unknown_key", "unknown_value")])
        ]

        # Expecting a KeyError since there's no handling for 'invalid_block'
        with self.assertRaises(TypeError):
            create_udmf_map(invalid_parser_output)


if __name__ == '__main__':
    unittest.main()
