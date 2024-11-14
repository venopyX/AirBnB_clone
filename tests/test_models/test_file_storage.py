import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.user = User()
        self.user.id = "1234"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john.doe@example.com"
        self.storage.new(self.user)
        self.storage.save()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method"""
        objects = self.storage.all()
        key = f"User.{self.user.id}"
        self.assertIn(key, objects)

    def test_new(self):
        """Test new method"""
        key = f"User.{self.user.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """Test reload method"""
        self.storage.reload()
        key = f"User.{self.user.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
