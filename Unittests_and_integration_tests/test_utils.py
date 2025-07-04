#!/usr/bin/env python3
'''Test utilities for github org client.'''

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Test utilities for github org client.'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(nested_map, path, expected):
        '''Test access_nested_map function with various inputs.'''
        unittest.assertEqual(access_nested_map(nested_map, path), expected)
