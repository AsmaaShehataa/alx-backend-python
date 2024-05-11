#!/usr/bin/env python3
"""First unit test for utils.access_nested_map."""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ("a",), None),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
