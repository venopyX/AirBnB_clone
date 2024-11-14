import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()
        self.review.text = "Great place!"

    def test_attributes(self):
        self.assertEqual(self.review.text, "Great place!")

    def test_class_name(self):
        self.assertEqual(self.review.__class__.__name__, "Review")


if __name__ == "__main__":
    unittest.main()
