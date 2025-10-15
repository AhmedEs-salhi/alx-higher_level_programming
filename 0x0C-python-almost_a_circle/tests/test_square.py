#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Square = __import__('models.square', fromlist=['Square']).Square

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Base = __import__('models.base', fromlist=['Base']).Base


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s3 = Square(1, 2, 3, 4)

    def testSquareInstance(self):
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s2, Square)
        self.assertIsInstance(self.s3, Square)

    def testExceptionRaised(self):
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "1")
        self.assertRaises(TypeError, Square, 1, 1, "1")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, 1, 1, -1)

    def testSquareStr(self):
        self.assertIsInstance(str(self.s1), str)
        self.assertEqual(str(self.s1), "[Square] ({}) 0/0 - 1".format(self.s1.id))
        self.assertEqual(str(self.s2), "[Square] ({}) 2/0 - 1".format(self.s2.id))
        self.assertEqual(str(self.s3), "[Square] ({}) 2/3 - 1".format(self.s3.id))

    def testSquareToDictionary(self):
        self.assertIsInstance(self.s1.to_dictionary(), dict)
        self.assertEqual(self.s1.to_dictionary(),  {'x': 0, 'y': 0, 'id': 68, 'size': 1})

    def testSquareUpdate(self):
        self.assertIsNone(self.s1.update(), None)
        self.assertIn("update", self.s1.__dir__())
        self.s1.update(98)
        self.assertEqual(self.s1.id, 98)
        self.s1.update(98, 1)
        self.assertEqual(self.s1.size, 1)
        self.s1.update(98, 1, 2)
        self.assertEqual(self.s1.x, 2)
        self.s1.update(98, 1, 2, 3)
        self.assertEqual(self.s1.y, 3)
        self.s1.update(**{"id": 89})
        self.assertEqual(self.s1.id, 89)
        self.s1.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.s1.size, 1)
        self.s1.update(**{'id': 89, 'size': 1024})
        self.assertEqual(self.s1.size, 1024)
        self.s1.update(**{'id': 89, 'size': 1024, 'x': 10})
        self.assertEqual(self.s1.x, 10)
        self.s1.update(**{'id': 89, 'size': 1024, 'x': 10, 'y': 4})
        self.assertEqual(self.s1.y, 4)

    def testSquareCreate(self):
        self.assertIn("create", self.s1.__dir__())
        self.assertEqual(Square.create(**{'id': 89}).id, 89)
        self.assertEqual(Square.create(**{'id': 89, 'size': 1}).size, 1)
        self.assertEqual(Square.create(**{'id': 89, 'size': 1, 'x': 10}).x, 10)
        self.assertEqual(Square.create(**{'id': 89, 'size': 1, 'x': 10, 'y': 3}).y, 3)

    def testRectangleSaveToFile(self):
        self.assertIn("save_to_file", self.s1.__dir__())
        self.assertIsNone(self.s1.save_to_file(None))
        self.assertIsNone(self.s1.save_to_file([]))
        self.assertIsNone(self.s1.save_to_file([Square(1, 2)]))

    def testRectangleFromFile(self):
        self.assertIsInstance(self.s2.load_from_file(), list)
        self.assertIsInstance(Base.load_from_file(), list)

    def tearDown(self):
        del self.s1
