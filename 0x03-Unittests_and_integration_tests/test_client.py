#!/usr/bin/env python3
"""
Test client
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, mock_get_json):
        """Test public_repos method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        test_class.repos_payload()
        test_class.public_repos()
        mock_get_json.assert_called_with(test_class._public_repos_url)

    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license(self, org_name, mock_get_json):
        """Test public_repos method with license"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        test_class.repos_payload()
        test_class.public_repos("license")
        mock_get_json.assert_called_with(test_class._public_repos_url)

    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD),
    ])
    @patch('client.get_json')
    def test_public_repos_without_license(self, org_name, mock_get_json):
        """Test public_repos method without license"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        test_class.repos_payload()
        test_class.public_repos(None)
        mock_get_json.assert_called_with(test_class._public_repos_url)

    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD),
    ])
    @patch('client.get_json')
    def test_has_license(self, org_name, mock_get_json):
        """Test has_license method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        test_class.repos_payload()
        test_class.has_license

    def test_public_repos_url(self):
        """Test public repos"""
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as my_mock:
            my_mock.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            test_repo_url = test_org._public_repos_url
            self.assertEqual(test_repo_url,
                             my_mock.return_value.get('repos_url'))
            my_mock.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'alx'},
                                            {'name': '89'},
                                            {'name': 'Holberton School'}])
    def test_public_repos(self, mock_repo):
        """Test public_repos method"""
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as my_mock:
            test_client = GithubOrgClient('holberton')
            test_repo = test_client.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_repo)
            mock_repo.assert_called_once()
            my_mock.assert_called_once()

    @parameterized.expand([
      ({"license": {"key": "my_license"}}, "my_license", True),
      ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, license_key, excpeted):
        """Test has_license method"""
        test_class = GithubOrgClient("alx")
        license_avail = test_class.has_license(repo, license_key)
        self.assertEqual(license_avail, excpeted)
