#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import os
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
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)


if __name__ == '__main__':
    unittest.main()
