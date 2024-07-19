# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from blllib import AdminApi

class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""
    test_json = {
        "client": {
            "name": "walter"
        }
    }

    def setUp(self) -> None:
        self.api = AdminApi()

    def tearDown(self) -> None:
        pass

    def test_client_create(self) -> None:
        """Test case for client_create

        """
        self.api.client_create(self.test_json)


    def test_client_delete(self) -> None:
        """Test case for client_delete

        """
        pass

    def test_client_list(self) -> None:
        """Test case for client_list

        """
        pass

    def test_client_revoke(self) -> None:
        """Test case for client_revoke

        """
        pass

    def test_ext_info_create(self) -> None:
        """Test case for ext_info_create

        """
        pass

    def test_ext_info_delete(self) -> None:
        """Test case for ext_info_delete

        """
        pass

    def test_ext_info_revoke(self) -> None:
        """Test case for ext_info_revoke

        """
        pass

    def test_koyo_create(self) -> None:
        """Test case for koyo_create

        Create new koyo information
        """
        pass

    def test_koyo_delete(self) -> None:
        """Test case for koyo_delete

        Delete koyo information
        """
        pass

    def test_koyo_revoke(self) -> None:
        """Test case for koyo_revoke

        Revoke koyo api key
        """
        pass

if __name__ == "__main__":
    unittest.main()
