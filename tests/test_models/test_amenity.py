import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "WiFi"

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "WiFi")

    def test_class_name(self):
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")


if __name__ == "__main__":
    unittest.main()
