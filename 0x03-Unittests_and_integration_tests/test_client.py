#!/usr/bin/env python3
"""
A module for testing the client module
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
        Test the org method
        """
        mock_get.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected)
    def test_public_repos_url(self):
        """Test th _public_repos_url property"""
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, mock_payload["repos_url"])
