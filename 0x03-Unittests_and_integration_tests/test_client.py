#!/usr/bin/env python3
"""
A module for testing the client module
"""
import unittest
from unittest.mock import patch, Mock, MagicMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public repos method"""
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=MagicMock
            ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            client = GithubOrgClient("google")
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
                )
