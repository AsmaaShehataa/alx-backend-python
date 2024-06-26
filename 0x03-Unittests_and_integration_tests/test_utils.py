#!/usr/bin/env python3
"""First unit test for utils.access_nested_map."""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test exception raised by access_nested_map."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test get_json function."""
        mock = Mock()
        mock.json.return_value = payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """Test class for memoize function."""

    def test_memoize(self):
        """Test memoize method."""
        class TestClass:
            """Test class self-descriptive."""
            def a_method(self):
                return 42

        @memoize
        def a_property(self):
            return self.a_method()
