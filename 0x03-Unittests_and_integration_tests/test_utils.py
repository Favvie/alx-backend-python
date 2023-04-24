#!/usr/bin/env python3
"""test utils.py file"""

from unittest.mock import patch
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test the access nested map with key path
        Raise a KeyError exception if key is invalid
        Parameters
        ----------
        nested_map: Mapping
        A nested map
        path: Sequence
        a sequence of key representing a path to the value
        expected
        expected result
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for testing get json using mock patch
    Inherits from unittest.TestCase class
    Parameters
    ----------
    unittest.TestCase
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Test the get json method in utils
        Parameters
        ----------
        test_url: string
        the url to be tested
        test_payload: dict
        expected url response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)
