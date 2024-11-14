import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()
        self.state.name = "California"

    def test_attributes(self):
        self.assertEqual(self.state.name, "California")

    def test_class_name(self):
        self.assertEqual(self.state.__class__.__name__, "State")


if __name__ == "__main__":
    unittest.main()
