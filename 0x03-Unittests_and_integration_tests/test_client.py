#!/usr/bin/env python3
"""
A module for testing the client module
"""
import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
        }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing class for GithubOrgClient"""
    @classmethod
    def setUpClass(cls):
        """set up mock for request.get"""
        cls.get_patcher = patch('request.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return cls.org_payload
        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method integration"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.mock_get.assert_called_with(self.org_payload["repos_url"])

    def test_apache2_repos(self):
        """Test filtering by Apache 2.0 license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.test_apache2_repos
        )
        self.mock_get.assert_called_with(self.org_payload["repos_url"])
