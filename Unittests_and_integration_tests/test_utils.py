#!/usr/bin/env python3
"""
Unit tests for utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        """Tests exceptions raised by access_nested_map"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], key)


class TestGetJson(unittest.TestCase):
    """
    Test for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests the get_json function"""
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test for the memoize decorator.
    """

    def test_memoize(self):
        """Tests that memoize caches the result of a method."""
        class TestClass:
            """A test class with a memoized property."""

            def a_method(self):
                """A method that returns a constant value."""
                return 42

            @memoize
            def a_property(self):
                """
                A property that is memoized. It calls a_method to get its value
                but should only do so on the first access.
                """
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            instance = TestClass()
            first_call_result = instance.a_property
            second_call_result = instance.a_property
            self.assertEqual(first_call_result, 42)
            self.assertEqual(second_call_result, 42)
            mock_method.assert_called_once()
