import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()
        self.place.name = "Cozy Cottage"
        self.place.city_id = "SFO"
        self.place.number_rooms = 2

    def test_attributes(self):
        self.assertEqual(self.place.name, "Cozy Cottage")
        self.assertEqual(self.place.city_id, "SFO")
        self.assertEqual(self.place.number_rooms, 2)

    def test_class_name(self):
        self.assertEqual(self.place.__class__.__name__, "Place")


if __name__ == "__main__":
    unittest.main()
