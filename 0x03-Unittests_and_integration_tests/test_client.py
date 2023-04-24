#!/usr/bin/env python3
"""Test Client Module"""

import unittest
from parameterized import parameterized
from utils import get_json
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, payload, mock_get_json):
        mock_get_json.return_value = payload

        client = GithubOrgClient(org_name)
        response = client.org

        self.assertEqual(response, mock_get_json.return_value)
        mock_get_json.\
            assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
