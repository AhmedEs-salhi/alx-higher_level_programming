#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Rectangle = __import__('models.rectangle', fromlist=['Rectangle']).Rectangle

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Base = __import__('models.base', fromlist=['Base']).Base

class TestToJsonFile(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.b = Base(9)

    def test_to_json_string(self):
        self.assertIsInstance(self.r, Rectangle)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 3}]), '[{"id": 3}]')
        self.assertIs(type(Base.to_json_string([{"id": 3}])), str)

    def tearDown(self):
        del self.r
