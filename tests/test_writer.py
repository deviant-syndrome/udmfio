import unittest

from udmfio import Linedef, Thing
from udmfio.writer import UDMFLinedef, UDMFThing


class TestUDMFStringification(unittest.TestCase):

    def test_udmf_linedef_stringification(self):
        # 1. Create an instance of the base class (assuming Linedef has attributes id, start, and end)
        linedef = Linedef()
        linedef.v1 = 0
        linedef.v2 = 1

        # 2. Convert this instance to UDMFLinedef
        udmf_linedef = UDMFLinedef(linedef)

        # 3. Obtain the UDMF string representation
        udmf_string = udmf_linedef.to_udmf_string()

        # 4. Compare the resulting string to the expected UDMF representation
        expected_string = """linedef
{
  v1=0;
  v2=1;
}
"""
        self.assertEqual(udmf_string, expected_string)

    def test_udmf_thing_stringification(self):
        # 1. Create an instance of the base class (assuming Thing has attributes id, type, x, y, and angle)
        thing = Thing()
        thing.type = 3004
        thing.x = -64.0
        thing.y = 64.0
        thing.angle = 90

        # 2. Convert this instance to UDMFThing
        udmf_thing = UDMFThing(thing)

        # 3. Obtain the UDMF string representation
        udmf_string = udmf_thing.to_udmf_string()

        # 4. Compare the resulting string to the expected UDMF representation
        expected_string = """thing
{
  x=-64.0;
  y=64.0;
  angle=90;
  type=3004;
}
"""
        self.assertEqual(udmf_string, expected_string)


# If you want to run the test
if __name__ == '__main__':
    unittest.main()
