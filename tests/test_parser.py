import unittest
from udmfio.parser import parse_udmf
from io import StringIO


class TestUDMFParser(unittest.TestCase):

    def test_simple_valid_input(self):
        input_data = """
        // This is a comment
        thing {
            id = 1;
            type = 3004;
            x = -64.0;
            y = 64.0;
            angle = 90;
        }
        """  # One of the positive scenarios
        expected_output = [('thing', [('id', 1), ('type', 3004), ('x', -64.0), ('y', 64.0), ('angle', 90)])]
        actual_output = parse_udmf(StringIO(input_data))
        self.assertEqual(expected_output, actual_output)

    def test_multiple_thing_definitions(self):
        input_data = """
        thing {
            id = 1;
            type = 3004;
            x = -64.0;
            y = 64.0;
            angle = 90;
        }
        thing {
            id = 2;
            type = 3005;
            x = 32.0;
            y = -32.0;
            angle = 180;
        }
        """
        expected_output = [
            ('thing', [('id', 1), ('type', 3004), ('x', -64.0), ('y', 64.0), ('angle', 90)]),
            ('thing', [('id', 2), ('type', 3005), ('x', 32.0), ('y', -32.0), ('angle', 180)])
        ]
        actual_output = parse_udmf(StringIO(input_data))
        self.assertEqual(expected_output, actual_output)

    def test_mixed_definitions(self):
        input_data = """
        thing {
            id = 1;
            type = 3004;
            x = -64.0;
            y = 64.0;
        }
        linedef {
            id = 1;
            v1 = 0;
            v2 = 1;
            sidefront = 1;
        }
        """
        expected_output = [
            ('thing', [('id', 1), ('type', 3004), ('x', -64.0), ('y', 64.0)]),
            ('linedef', [('id', 1), ('v1', 0), ('v2', 1), ('sidefront', 1)])
        ]
        actual_output = parse_udmf(StringIO(input_data))
        self.assertEqual(expected_output, actual_output)

    def test_varied_data_types(self):
        input_data = """
        thing {
            id = 1;
            type = 3004;
            texture = "SKY";
            x = -64.0;
            y = 64.0;
        }
        """
        expected_output = [
            ('thing', [('id', 1), ('type', 3004), ('texture', "SKY"), ('x', -64.0), ('y', 64.0)])
        ]
        actual_output = parse_udmf(StringIO(input_data))
        self.assertEqual(expected_output, actual_output)

    def test_missing_semicolon(self):
        input_data = """
        thing {
            id = 1
            type = 3004;
        }
        """  # One of the negative scenarios
        with self.assertRaises(SyntaxError):  # Assuming a SyntaxError is raised for parsing errors
            parse_udmf(StringIO(input_data))

    def test_missing_closing_brace(self):
        input_data = """
        thing {
            id = 1;
            type = 3004;
            x = -64.0;
            y = 64.0;
            angle = 90;
        """
        with self.assertRaises(SyntaxError):
            parse_udmf(StringIO(input_data))

    def test_unexpected_token(self):
        input_data = """
        thing {
            id = 1;
            #!
        }
        """
        with self.assertRaises(SyntaxError):
            parse_udmf(StringIO(input_data))


if __name__ == "__main__":
    unittest.main()
