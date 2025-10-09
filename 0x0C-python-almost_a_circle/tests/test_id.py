#!/usr/bin/python3

import unittest
import sys, os
from stringprep import b1_set

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Base = __import__('models.base', fromlist=['Base']).Base

class TestIdIncrementation(unittest.TestCase):
    def setUp(self):
        self.b = Base(98)
        self.b1 = Base()
        self.b2 = Base(1024)
        self.b3 = Base()

    def test_base_instantiation(self):
        self.assertIsInstance(self.b1, Base)
        self.assertIsInstance(self.b2, Base)
        self.assertIsInstance(self.b3, Base)

    def test_id_incrementation(self):
        self.assertEqual(self.b.id, 98)
        self.assertEqual(self.b1.id, 3)
        self.assertEqual(self.b2.id, 1024)
        self.assertEqual(self.b3.id, 4)

    def tearDown(self):
        del self.b
        del self.b1
        del self.b2
        del self.b3