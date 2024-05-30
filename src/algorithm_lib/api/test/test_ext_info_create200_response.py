# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ext_info_create200_response import ExtInfoCreate200Response

class TestExtInfoCreate200Response(unittest.TestCase):
    """ExtInfoCreate200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtInfoCreate200Response:
        """Test ExtInfoCreate200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtInfoCreate200Response`
        """
        model = ExtInfoCreate200Response()
        if include_optional:
            return ExtInfoCreate200Response(
                external_id = 'HOGE_ID',
                external_name = '',
                external_description = '',
                first_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_history = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                bearer_token = ''
            )
        else:
            return ExtInfoCreate200Response(
                external_id = 'HOGE_ID',
                external_name = '',
                external_description = '',
                first_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_history = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                bearer_token = '',
        )
        """

    def testExtInfoCreate200Response(self):
        """Test ExtInfoCreate200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
