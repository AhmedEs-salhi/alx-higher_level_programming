#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This is my unittest class
    """
    def test_normal_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_float(self):
        self.assertEqual(max_integer([4.4, 1.2, 2.1, 3.8]), 4.4)
        
    def test_max_char_in_string(self):
        self.assertEqual(max_integer("Ahmedz"), 'z')
        
    def test_max_char_charList(self):
        self.assertEqual(max_integer(["A", "z", "b", "c"]), 'z')

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        
    def test_None_list(self):
        self.assertRaises(TypeError, max_integer, None)
    
    def test_matrix(self):
        self.assertRaises(TypeError, max_integer, [[12, 4, 5], 12, ['s', '2']])
        
    def test_negative_values(self):
        self.assertEqual(max_integer([-1, -4, -9, -2]), -1)
        
    def test_one_element_list(self):
        self.assertEqual(max_integer([9]), 9)
    
    def test_same_values(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        
    def test_floats_and_ints(self):
        self.assertEqual(max_integer([1, 3.2, 9, 0, 12.3]), 12.3)
    
    def test_NaN_list(self):
        self.assertRaises(TypeError, max_integer, float('nan'))