# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.auth_api import AuthApi


class TestAuthApi(unittest.TestCase):
    """ AuthApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.auth_api.AuthApi()

    def tearDown(self):
        pass

    def test_create_oidc_test_config(self):
        """
        Test case for create_oidc_test_config

        Create OIDC Test Configuration
        """
        pass

    def test_create_saml_test_config(self):
        """
        Test case for create_saml_test_config

        Create SAML Test Configuration
        """
        pass

    def test_delete_oidc_test_config(self):
        """
        Test case for delete_oidc_test_config

        Delete OIDC Test Configuration
        """
        pass

    def test_delete_saml_test_config(self):
        """
        Test case for delete_saml_test_config

        Delete SAML Test Configuration
        """
        pass

    def test_fetch_and_parse_saml_idp_metadata(self):
        """
        Test case for fetch_and_parse_saml_idp_metadata

        Parse SAML IdP Url
        """
        pass

    def test_ldap_config(self):
        """
        Test case for ldap_config

        Get LDAP Configuration
        """
        pass

    def test_oidc_config(self):
        """
        Test case for oidc_config

        Get OIDC Configuration
        """
        pass

    def test_oidc_test_config(self):
        """
        Test case for oidc_test_config

        Get OIDC Test Configuration
        """
        pass

    def test_parse_saml_idp_metadata(self):
        """
        Test case for parse_saml_idp_metadata

        Parse SAML IdP XML
        """
        pass

    def test_saml_config(self):
        """
        Test case for saml_config

        Get SAML Configuration
        """
        pass

    def test_saml_test_config(self):
        """
        Test case for saml_test_config

        Get SAML Test Configuration
        """
        pass

    def test_test_ldap_config_auth(self):
        """
        Test case for test_ldap_config_auth

        Test LDAP Auth
        """
        pass

    def test_test_ldap_config_connection(self):
        """
        Test case for test_ldap_config_connection

        Test LDAP Connection
        """
        pass

    def test_test_ldap_config_user_auth(self):
        """
        Test case for test_ldap_config_user_auth

        Test LDAP User Auth
        """
        pass

    def test_test_ldap_config_user_info(self):
        """
        Test case for test_ldap_config_user_info

        Test LDAP User Info
        """
        pass

    def test_update_ldap_config(self):
        """
        Test case for update_ldap_config

        Update LDAP Configuration
        """
        pass

    def test_update_oidc_config(self):
        """
        Test case for update_oidc_config

        Update OIDC Configuration
        """
        pass

    def test_update_saml_config(self):
        """
        Test case for update_saml_config

        Update SAML Configuration
        """
        pass


if __name__ == '__main__':
    unittest.main()
