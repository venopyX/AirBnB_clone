#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import json
import re


class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instantiation(self):
        """Tests instantiation of BaseModel class."""
        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        """Tests for unique user ids."""
        nl = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(nl)), len(nl))  # Ensures unique IDs

    def test_save(self):
        """Tests the public instance method save()."""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        """Tests for __str__ method."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_to_dict(self):
        """Tests the public instance method to_dict()."""
        b = BaseModel()
        b.name = "Laura"
        b.age = 23
        d = b.to_dict()
        self.assertEqual(d["name"], "Laura")
        self.assertEqual(d["age"], 23)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    def test_from_dict(self):
        """Tests creating an instance from a dictionary (kwargs)."""
        b = BaseModel()
        b.name = "Laura"
        b.age = 23
        dict_repr = b.to_dict()

        dict_repr.pop('id', None)

        new_instance = BaseModel(**dict_repr)
        self.assertEqual(new_instance.name, "Laura")
        self.assertEqual(new_instance.age, 23)
        self.assertEqual(type(new_instance.created_at), datetime)
        self.assertEqual(type(new_instance.updated_at), datetime)
        self.assertNotEqual(b.id, new_instance.id)  # Ensure IDs are unique

    def test_datetime_conversion_in_kwargs(self):
        """Test conversion of datetime strings in kwargs."""
        b = BaseModel()
        dict_repr = b.to_dict()
        dict_repr["created_at"] = "2024-11-13T00:00:00.000000"
        dict_repr["updated_at"] = "2024-11-13T00:00:00.000000"
        del dict_repr["__class__"]

        new_instance = BaseModel(**dict_repr)
        self.assertEqual(new_instance.created_at, datetime(2024, 11, 13, 0, 0, 0))
        self.assertEqual(new_instance.updated_at, datetime(2024, 11, 13, 0, 0, 0))

if __name__ == "__main__":
    unittest.main()
