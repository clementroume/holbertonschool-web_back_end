#!/usr/bin/env python3
"""Unit tests for client.py"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        """Test the org method."""
        payload = {"login": org, "id": 42}
        mock_get_json.return_value = payload

        client_instance = GithubOrgClient(org)
        result = client_instance.org
        expected_url = f"https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, payload)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property."""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test/repos"}
        client_instance = GithubOrgClient("test")
        self.assertEqual(client_instance._public_repos_url,
                         "https://api.github.com/orgs/test/repos")

    @patch("client.get_json")
    @patch(
        "client.GithubOrgClient._public_repos_url",
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method."""
        test_repos_url = "https://api.github.com/test_url/repos"
        mock_public_repos_url.return_value = test_repos_url

        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get_json.return_value = test_payload

        client_instance = GithubOrgClient("test")
        repos = client_instance.public_repos()

        self.assertEqual(repos, ["repo1", "repo2"])

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(test_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method returns the correct boolean."""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test suite for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class fixture by patching requests.get."""
        config = {
            "return_value.json.side_effect": [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }

        cls.get_patcher = patch("requests.get", **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class fixture by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos without a license filter."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with a license filter."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
