#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Rectangle = __import__('models.rectangle', fromlist=['Rectangle']).Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(1, 2, 3, 4)
        self.r4 = Rectangle(1, 2, 3, 4, 5)

    def testIsRectangleInstance(self):
        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r2, Rectangle)
        self.assertIsInstance(self.r3, Rectangle)
        self.assertIsInstance(self.r4, Rectangle)

    def testRectangleStr(self):
        self.assertEqual(str(self.r1), "[Rectangle] ({}) 0/0 - 1/2".format(self.r1.id))
        self.assertEqual(str(self.r2), "[Rectangle] ({}) 3/0 - 1/2".format(self.r2.id))
        self.assertEqual(str(self.r3), "[Rectangle] ({}) 3/4 - 1/2".format(self.r3.id))
        self.assertEqual(str(self.r4), "[Rectangle] (5) 3/4 - 1/2")

    def testRectangleArea(self):
        self.assertEqual(self.r1.area(), 2)

    def testRectangleDisplay(self):
        self.assertIn("display", self.r1.__dir__())
        self.assertIs(self.r1.display(), None)
        self.assertIs(self.r2.display(), None)
        self.assertIs(self.r3.display(), None)

    def testRectangleToDictionary(self):
        self.assertIn("to_dictionary", self.r1.__dir__())
        self.assertEqual(self.r1.to_dictionary(), {'x': 0, 'y': 0, 'id': self.r1.id, 'width': 1, "height": 2})

    def testRectangleToUpdate(self):
        self.assertIn("update", self.r1.__dir__())
        self.r1.update(98)
        self.assertEqual(self.r1.id, 98)
        self.r1.update(98, 1)
        self.assertEqual(self.r1.width, 1)
        self.r1.update(98, 1, 2)
        self.assertEqual(self.r1.height, 2)
        self.r1.update(98, 1, 2, 3)
        self.assertEqual(self.r1.x, 3)
        self.r1.update(98, 1, 2, 3, 6)
        self.assertEqual(self.r1.y, 6)
        self.r1.update(**{"id": 89})
        self.assertEqual(self.r1.id, 89)
        self.r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(self.r1.width, 1)
        self.r1.update(**{'id': 89, 'width': 1, 'height': 22})
        self.assertEqual(self.r1.height, 22)
        self.r1.update(**{'id': 89, 'width': 1, 'height': 22, 'x': 10})
        self.assertEqual(self.r1.x, 10)
        self.r1.update(**{'id': 89, 'width': 1, 'height': 22, 'x': 10, 'y': 4})
        self.assertEqual(self.r1.y, 4)

    def testRectangleCreate(self):
        self.assertIn("create", self.r1.__dir__())
        self.assertEqual(Rectangle.create(**{'id': 89}).id, 89)
        self.assertEqual(Rectangle.create(**{'id': 89, 'width': 1}).width, 1)
        self.assertEqual(Rectangle.create(**{'id': 89, 'width': 1, 'height': 22}).height, 22)
        self.assertEqual(Rectangle.create(**{'id': 89, 'width': 1, 'height': 22, 'x': 10}).x, 10)
        self.assertEqual(Rectangle.create(**{'id': 89, 'width': 1, 'height': 22, 'x': 10, 'y': 3}).y, 3)

    def testRectangleSaveToFile(self):
        pass
        #self.assertIn("save_to_file", self.r1.__dir__())
        #self.assertIsNone(Rectangle.save_to_file(None))
        #self.assertIsNone(Rectangle.save_to_file([]))
        #self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))

    def testRectangleFromFile(self):
        self.assertIsInstance(self.r1.load_from_file(), list)

    def testRectangleExceptionRaised(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, "1")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "1")
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3
        del self.r4