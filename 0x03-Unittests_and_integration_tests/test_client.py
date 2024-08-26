#!/usr/bin/env python3
"""
Test for client
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get):
        """
        method for test org
        """
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")
        self.assertEqual(result, expected)
