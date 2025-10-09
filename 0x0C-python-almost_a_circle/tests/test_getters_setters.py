#!/usr/bin/python3
import sys, os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Rectangle = __import__('models.rectangle', fromlist=['Rectangle']).Rectangle


class TestGettersSetters(unittest.TestCase):
    def testInstantiation(self):
        self.r1 = Rectangle(10, 20)
        self.assertIsInstance(self.r1, Rectangle)
        self.r2 = Rectangle(5, 10)
        self.assertIsInstance(self.r2, Rectangle)
        self.r3 = Rectangle(3, 1)
        self.assertIsInstance(self.r3, Rectangle)

    def testGettersSettersR1(self):
        self.r1 = Rectangle(10, 20, 23, 24)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 20)
        self.assertEqual(self.r1.x, 23)
        self.assertEqual(self.r1.y, 24)
        self.assertEqual(self.r1.id, 1)

    def testGettersSettersR2(self):
        self.r2 = Rectangle(10, 20, 99, 88, 100)
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 20)
        self.assertEqual(self.r2.x, 99)
        self.assertEqual(self.r2.y, 88)
        self.assertEqual(self.r2.id, 100)
        self.r3 = Rectangle(10, 22)
        self.assertEqual(self.r3.id, 2)
