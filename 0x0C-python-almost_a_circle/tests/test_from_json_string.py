#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
Rectangle = __import__('models.rectangle', fromlist=['Rectangle']).Rectangle

class TestFromJsonString(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.list_output = Rectangle.to_json_string([
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ])

    def test_from_json_file(self):
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string([]), [])
        self.assertIs(type(Rectangle.from_json_string([])), list)
        self.assertEqual(Rectangle.from_json_string(self.list_output), [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Rectangle.from_json_string('[{"id": 98}]'), [{"id": 98}])


    def tearDown(self):
        del self.r