#!/usr/bin/python3

import unittest
import sys, os
from stringprep import b1_set

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Base = __import__('models.base', fromlist=['Base']).Base

class TestIdIncrementation(unittest.TestCase):
    def setUp(self):
        pass

    def test_base_instantiation(self):
        self.b = Base(98)
        self.assertIsInstance(self.b, Base)
        self.b = Base(98)
        self.assertIsInstance(self.b, Base)
        self.b = Base(98)
        self.assertIsInstance(self.b, Base)

    def test_id_incrementation(self):
        self.b = Base(98)
        self.assertEqual(self.b.id, 98)
        self.b = Base()
        self.assertEqual(self.b.id, 6)
        self.b = Base(1024)
        self.assertEqual(self.b.id, 1024)
        self.b = Base()
        self.assertEqual(self.b.id, 7)

    def tearDown(self):
        del self.b
