import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"

    def test_attributes(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)

    def test_class_name(self):
        self.assertEqual(self.user.__class__.__name__, "User")


if __name__ == "__main__":
    unittest.main()
