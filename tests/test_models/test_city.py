import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "CA"

    def test_attributes(self):
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "CA")

    def test_class_name(self):
        self.assertEqual(self.city.__class__.__name__, "City")


if __name__ == "__main__":
    unittest.main()
