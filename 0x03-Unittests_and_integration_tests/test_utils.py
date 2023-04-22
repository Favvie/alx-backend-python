#!/usr/bin/env python3
"""test utils.py file"""


import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing accessed nested map function
    Inherits from unittest.TestCase class
    Parameters
    ----------
    unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)

    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the access nested map with key path.
        Parameters
        ----------
        nested_map: Mapping
        A nested map
        path: Sequence
        a sequence of key representing a path to the value
        expected
        expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
