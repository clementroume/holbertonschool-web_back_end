#!/usr/bin/env python3
"""Unit tests for client.py"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


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
        result = client_instance.org()
        expected_url = f"https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, payload)
