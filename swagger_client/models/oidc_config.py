# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OIDCConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, enabled=None, identifier=None, secret=None, scopes=None, issuer=None, audience=None, authorization_endpoint=None, token_endpoint=None, userinfo_endpoint=None, user_attribute_map_email=None, user_attribute_map_first_name=None, user_attribute_map_last_name=None, new_user_migration_types=None, alternate_email_login_allowed=None, test_slug=None, modified_at=None, modified_by=None, default_new_user_roles=None, default_new_user_groups=None, default_new_user_role_ids=None, default_new_user_group_ids=None, set_roles_from_groups=None, groups_attribute=None, groups=None, groups_with_role_ids=None, auth_requires_role=None, user_attributes=None, user_attributes_with_ids=None, url=None, can=None):
        """
        OIDCConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'identifier': 'str',
            'secret': 'str',
            'scopes': 'list[str]',
            'issuer': 'str',
            'audience': 'str',
            'authorization_endpoint': 'str',
            'token_endpoint': 'str',
            'userinfo_endpoint': 'str',
            'user_attribute_map_email': 'str',
            'user_attribute_map_first_name': 'str',
            'user_attribute_map_last_name': 'str',
            'new_user_migration_types': 'str',
            'alternate_email_login_allowed': 'bool',
            'test_slug': 'str',
            'modified_at': 'str',
            'modified_by': 'str',
            'default_new_user_roles': 'list[Role]',
            'default_new_user_groups': 'list[Group]',
            'default_new_user_role_ids': 'list[int]',
            'default_new_user_group_ids': 'list[int]',
            'set_roles_from_groups': 'bool',
            'groups_attribute': 'str',
            'groups': 'list[OIDCGroupRead]',
            'groups_with_role_ids': 'list[OIDCGroupWrite]',
            'auth_requires_role': 'bool',
            'user_attributes': 'list[OIDCUserAttributeRead]',
            'user_attributes_with_ids': 'list[OIDCUserAttributeWrite]',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'identifier': 'identifier',
            'secret': 'secret',
            'scopes': 'scopes',
            'issuer': 'issuer',
            'audience': 'audience',
            'authorization_endpoint': 'authorization_endpoint',
            'token_endpoint': 'token_endpoint',
            'userinfo_endpoint': 'userinfo_endpoint',
            'user_attribute_map_email': 'user_attribute_map_email',
            'user_attribute_map_first_name': 'user_attribute_map_first_name',
            'user_attribute_map_last_name': 'user_attribute_map_last_name',
            'new_user_migration_types': 'new_user_migration_types',
            'alternate_email_login_allowed': 'alternate_email_login_allowed',
            'test_slug': 'test_slug',
            'modified_at': 'modified_at',
            'modified_by': 'modified_by',
            'default_new_user_roles': 'default_new_user_roles',
            'default_new_user_groups': 'default_new_user_groups',
            'default_new_user_role_ids': 'default_new_user_role_ids',
            'default_new_user_group_ids': 'default_new_user_group_ids',
            'set_roles_from_groups': 'set_roles_from_groups',
            'groups_attribute': 'groups_attribute',
            'groups': 'groups',
            'groups_with_role_ids': 'groups_with_role_ids',
            'auth_requires_role': 'auth_requires_role',
            'user_attributes': 'user_attributes',
            'user_attributes_with_ids': 'user_attributes_with_ids',
            'url': 'url',
            'can': 'can'
        }

        self._enabled = enabled
        self._identifier = identifier
        self._secret = secret
        self._scopes = scopes
        self._issuer = issuer
        self._audience = audience
        self._authorization_endpoint = authorization_endpoint
        self._token_endpoint = token_endpoint
        self._userinfo_endpoint = userinfo_endpoint
        self._user_attribute_map_email = user_attribute_map_email
        self._user_attribute_map_first_name = user_attribute_map_first_name
        self._user_attribute_map_last_name = user_attribute_map_last_name
        self._new_user_migration_types = new_user_migration_types
        self._alternate_email_login_allowed = alternate_email_login_allowed
        self._test_slug = test_slug
        self._modified_at = modified_at
        self._modified_by = modified_by
        self._default_new_user_roles = default_new_user_roles
        self._default_new_user_groups = default_new_user_groups
        self._default_new_user_role_ids = default_new_user_role_ids
        self._default_new_user_group_ids = default_new_user_group_ids
        self._set_roles_from_groups = set_roles_from_groups
        self._groups_attribute = groups_attribute
        self._groups = groups
        self._groups_with_role_ids = groups_with_role_ids
        self._auth_requires_role = auth_requires_role
        self._user_attributes = user_attributes
        self._user_attributes_with_ids = user_attributes_with_ids
        self._url = url
        self._can = can

    @property
    def enabled(self):
        """
        Gets the enabled of this OIDCConfig.
        Enable/Disable OIDC authentication for the server

        :return: The enabled of this OIDCConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this OIDCConfig.
        Enable/Disable OIDC authentication for the server

        :param enabled: The enabled of this OIDCConfig.
        :type: bool
        """

        self._enabled = enabled

    @property
    def identifier(self):
        """
        Gets the identifier of this OIDCConfig.
        Relying Party Identifier (provided by OpenID Provider)

        :return: The identifier of this OIDCConfig.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this OIDCConfig.
        Relying Party Identifier (provided by OpenID Provider)

        :param identifier: The identifier of this OIDCConfig.
        :type: str
        """

        self._identifier = identifier

    @property
    def secret(self):
        """
        Gets the secret of this OIDCConfig.
        (Write-Only) Relying Party Secret (provided by OpenID Provider)

        :return: The secret of this OIDCConfig.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this OIDCConfig.
        (Write-Only) Relying Party Secret (provided by OpenID Provider)

        :param secret: The secret of this OIDCConfig.
        :type: str
        """

        self._secret = secret

    @property
    def scopes(self):
        """
        Gets the scopes of this OIDCConfig.
        Array of scopes to request.

        :return: The scopes of this OIDCConfig.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this OIDCConfig.
        Array of scopes to request.

        :param scopes: The scopes of this OIDCConfig.
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def issuer(self):
        """
        Gets the issuer of this OIDCConfig.
        OpenID Provider Issuer

        :return: The issuer of this OIDCConfig.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this OIDCConfig.
        OpenID Provider Issuer

        :param issuer: The issuer of this OIDCConfig.
        :type: str
        """

        self._issuer = issuer

    @property
    def audience(self):
        """
        Gets the audience of this OIDCConfig.
        OpenID Provider Audience

        :return: The audience of this OIDCConfig.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """
        Sets the audience of this OIDCConfig.
        OpenID Provider Audience

        :param audience: The audience of this OIDCConfig.
        :type: str
        """

        self._audience = audience

    @property
    def authorization_endpoint(self):
        """
        Gets the authorization_endpoint of this OIDCConfig.
        OpenID Provider Authorization Url

        :return: The authorization_endpoint of this OIDCConfig.
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        """
        Sets the authorization_endpoint of this OIDCConfig.
        OpenID Provider Authorization Url

        :param authorization_endpoint: The authorization_endpoint of this OIDCConfig.
        :type: str
        """

        self._authorization_endpoint = authorization_endpoint

    @property
    def token_endpoint(self):
        """
        Gets the token_endpoint of this OIDCConfig.
        OpenID Provider Token Url

        :return: The token_endpoint of this OIDCConfig.
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        """
        Sets the token_endpoint of this OIDCConfig.
        OpenID Provider Token Url

        :param token_endpoint: The token_endpoint of this OIDCConfig.
        :type: str
        """

        self._token_endpoint = token_endpoint

    @property
    def userinfo_endpoint(self):
        """
        Gets the userinfo_endpoint of this OIDCConfig.
        OpenID Provider User Information Url

        :return: The userinfo_endpoint of this OIDCConfig.
        :rtype: str
        """
        return self._userinfo_endpoint

    @userinfo_endpoint.setter
    def userinfo_endpoint(self, userinfo_endpoint):
        """
        Sets the userinfo_endpoint of this OIDCConfig.
        OpenID Provider User Information Url

        :param userinfo_endpoint: The userinfo_endpoint of this OIDCConfig.
        :type: str
        """

        self._userinfo_endpoint = userinfo_endpoint

    @property
    def user_attribute_map_email(self):
        """
        Gets the user_attribute_map_email of this OIDCConfig.
        Name of user record attributes used to indicate email address field

        :return: The user_attribute_map_email of this OIDCConfig.
        :rtype: str
        """
        return self._user_attribute_map_email

    @user_attribute_map_email.setter
    def user_attribute_map_email(self, user_attribute_map_email):
        """
        Sets the user_attribute_map_email of this OIDCConfig.
        Name of user record attributes used to indicate email address field

        :param user_attribute_map_email: The user_attribute_map_email of this OIDCConfig.
        :type: str
        """

        self._user_attribute_map_email = user_attribute_map_email

    @property
    def user_attribute_map_first_name(self):
        """
        Gets the user_attribute_map_first_name of this OIDCConfig.
        Name of user record attributes used to indicate first name

        :return: The user_attribute_map_first_name of this OIDCConfig.
        :rtype: str
        """
        return self._user_attribute_map_first_name

    @user_attribute_map_first_name.setter
    def user_attribute_map_first_name(self, user_attribute_map_first_name):
        """
        Sets the user_attribute_map_first_name of this OIDCConfig.
        Name of user record attributes used to indicate first name

        :param user_attribute_map_first_name: The user_attribute_map_first_name of this OIDCConfig.
        :type: str
        """

        self._user_attribute_map_first_name = user_attribute_map_first_name

    @property
    def user_attribute_map_last_name(self):
        """
        Gets the user_attribute_map_last_name of this OIDCConfig.
        Name of user record attributes used to indicate last name

        :return: The user_attribute_map_last_name of this OIDCConfig.
        :rtype: str
        """
        return self._user_attribute_map_last_name

    @user_attribute_map_last_name.setter
    def user_attribute_map_last_name(self, user_attribute_map_last_name):
        """
        Sets the user_attribute_map_last_name of this OIDCConfig.
        Name of user record attributes used to indicate last name

        :param user_attribute_map_last_name: The user_attribute_map_last_name of this OIDCConfig.
        :type: str
        """

        self._user_attribute_map_last_name = user_attribute_map_last_name

    @property
    def new_user_migration_types(self):
        """
        Gets the new_user_migration_types of this OIDCConfig.
        Merge first-time oidc login to existing user account by email addresses. When a user logs in for the first time via oidc this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'

        :return: The new_user_migration_types of this OIDCConfig.
        :rtype: str
        """
        return self._new_user_migration_types

    @new_user_migration_types.setter
    def new_user_migration_types(self, new_user_migration_types):
        """
        Sets the new_user_migration_types of this OIDCConfig.
        Merge first-time oidc login to existing user account by email addresses. When a user logs in for the first time via oidc this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'

        :param new_user_migration_types: The new_user_migration_types of this OIDCConfig.
        :type: str
        """

        self._new_user_migration_types = new_user_migration_types

    @property
    def alternate_email_login_allowed(self):
        """
        Gets the alternate_email_login_allowed of this OIDCConfig.
        Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.

        :return: The alternate_email_login_allowed of this OIDCConfig.
        :rtype: bool
        """
        return self._alternate_email_login_allowed

    @alternate_email_login_allowed.setter
    def alternate_email_login_allowed(self, alternate_email_login_allowed):
        """
        Sets the alternate_email_login_allowed of this OIDCConfig.
        Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.

        :param alternate_email_login_allowed: The alternate_email_login_allowed of this OIDCConfig.
        :type: bool
        """

        self._alternate_email_login_allowed = alternate_email_login_allowed

    @property
    def test_slug(self):
        """
        Gets the test_slug of this OIDCConfig.
        Slug to identify configurations that are created in order to run a OIDC config test

        :return: The test_slug of this OIDCConfig.
        :rtype: str
        """
        return self._test_slug

    @test_slug.setter
    def test_slug(self, test_slug):
        """
        Sets the test_slug of this OIDCConfig.
        Slug to identify configurations that are created in order to run a OIDC config test

        :param test_slug: The test_slug of this OIDCConfig.
        :type: str
        """

        self._test_slug = test_slug

    @property
    def modified_at(self):
        """
        Gets the modified_at of this OIDCConfig.
        When this config was last modified

        :return: The modified_at of this OIDCConfig.
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this OIDCConfig.
        When this config was last modified

        :param modified_at: The modified_at of this OIDCConfig.
        :type: str
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """
        Gets the modified_by of this OIDCConfig.
        User id of user who last modified this config

        :return: The modified_by of this OIDCConfig.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this OIDCConfig.
        User id of user who last modified this config

        :param modified_by: The modified_by of this OIDCConfig.
        :type: str
        """

        self._modified_by = modified_by

    @property
    def default_new_user_roles(self):
        """
        Gets the default_new_user_roles of this OIDCConfig.
        (Read-only) Roles that will be applied to new users the first time they login via OIDC

        :return: The default_new_user_roles of this OIDCConfig.
        :rtype: list[Role]
        """
        return self._default_new_user_roles

    @default_new_user_roles.setter
    def default_new_user_roles(self, default_new_user_roles):
        """
        Sets the default_new_user_roles of this OIDCConfig.
        (Read-only) Roles that will be applied to new users the first time they login via OIDC

        :param default_new_user_roles: The default_new_user_roles of this OIDCConfig.
        :type: list[Role]
        """

        self._default_new_user_roles = default_new_user_roles

    @property
    def default_new_user_groups(self):
        """
        Gets the default_new_user_groups of this OIDCConfig.
        (Read-only) Groups that will be applied to new users the first time they login via OIDC

        :return: The default_new_user_groups of this OIDCConfig.
        :rtype: list[Group]
        """
        return self._default_new_user_groups

    @default_new_user_groups.setter
    def default_new_user_groups(self, default_new_user_groups):
        """
        Sets the default_new_user_groups of this OIDCConfig.
        (Read-only) Groups that will be applied to new users the first time they login via OIDC

        :param default_new_user_groups: The default_new_user_groups of this OIDCConfig.
        :type: list[Group]
        """

        self._default_new_user_groups = default_new_user_groups

    @property
    def default_new_user_role_ids(self):
        """
        Gets the default_new_user_role_ids of this OIDCConfig.
        (Write-Only) Array of ids of roles that will be applied to new users the first time they login via OIDC

        :return: The default_new_user_role_ids of this OIDCConfig.
        :rtype: list[int]
        """
        return self._default_new_user_role_ids

    @default_new_user_role_ids.setter
    def default_new_user_role_ids(self, default_new_user_role_ids):
        """
        Sets the default_new_user_role_ids of this OIDCConfig.
        (Write-Only) Array of ids of roles that will be applied to new users the first time they login via OIDC

        :param default_new_user_role_ids: The default_new_user_role_ids of this OIDCConfig.
        :type: list[int]
        """

        self._default_new_user_role_ids = default_new_user_role_ids

    @property
    def default_new_user_group_ids(self):
        """
        Gets the default_new_user_group_ids of this OIDCConfig.
        (Write-Only) Array of ids of groups that will be applied to new users the first time they login via OIDC

        :return: The default_new_user_group_ids of this OIDCConfig.
        :rtype: list[int]
        """
        return self._default_new_user_group_ids

    @default_new_user_group_ids.setter
    def default_new_user_group_ids(self, default_new_user_group_ids):
        """
        Sets the default_new_user_group_ids of this OIDCConfig.
        (Write-Only) Array of ids of groups that will be applied to new users the first time they login via OIDC

        :param default_new_user_group_ids: The default_new_user_group_ids of this OIDCConfig.
        :type: list[int]
        """

        self._default_new_user_group_ids = default_new_user_group_ids

    @property
    def set_roles_from_groups(self):
        """
        Gets the set_roles_from_groups of this OIDCConfig.
        Set user roles in Looker based on groups from OIDC

        :return: The set_roles_from_groups of this OIDCConfig.
        :rtype: bool
        """
        return self._set_roles_from_groups

    @set_roles_from_groups.setter
    def set_roles_from_groups(self, set_roles_from_groups):
        """
        Sets the set_roles_from_groups of this OIDCConfig.
        Set user roles in Looker based on groups from OIDC

        :param set_roles_from_groups: The set_roles_from_groups of this OIDCConfig.
        :type: bool
        """

        self._set_roles_from_groups = set_roles_from_groups

    @property
    def groups_attribute(self):
        """
        Gets the groups_attribute of this OIDCConfig.
        Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'

        :return: The groups_attribute of this OIDCConfig.
        :rtype: str
        """
        return self._groups_attribute

    @groups_attribute.setter
    def groups_attribute(self, groups_attribute):
        """
        Sets the groups_attribute of this OIDCConfig.
        Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'

        :param groups_attribute: The groups_attribute of this OIDCConfig.
        :type: str
        """

        self._groups_attribute = groups_attribute

    @property
    def groups(self):
        """
        Gets the groups of this OIDCConfig.
        (Read-only) Array of mappings between OIDC Groups and Looker Roles

        :return: The groups of this OIDCConfig.
        :rtype: list[OIDCGroupRead]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this OIDCConfig.
        (Read-only) Array of mappings between OIDC Groups and Looker Roles

        :param groups: The groups of this OIDCConfig.
        :type: list[OIDCGroupRead]
        """

        self._groups = groups

    @property
    def groups_with_role_ids(self):
        """
        Gets the groups_with_role_ids of this OIDCConfig.
        (Read/Write) Array of mappings between OIDC Groups and arrays of Looker Role ids

        :return: The groups_with_role_ids of this OIDCConfig.
        :rtype: list[OIDCGroupWrite]
        """
        return self._groups_with_role_ids

    @groups_with_role_ids.setter
    def groups_with_role_ids(self, groups_with_role_ids):
        """
        Sets the groups_with_role_ids of this OIDCConfig.
        (Read/Write) Array of mappings between OIDC Groups and arrays of Looker Role ids

        :param groups_with_role_ids: The groups_with_role_ids of this OIDCConfig.
        :type: list[OIDCGroupWrite]
        """

        self._groups_with_role_ids = groups_with_role_ids

    @property
    def auth_requires_role(self):
        """
        Gets the auth_requires_role of this OIDCConfig.
        Users will not be allowed to login at all unless a role for them is found in OIDC if set to true

        :return: The auth_requires_role of this OIDCConfig.
        :rtype: bool
        """
        return self._auth_requires_role

    @auth_requires_role.setter
    def auth_requires_role(self, auth_requires_role):
        """
        Sets the auth_requires_role of this OIDCConfig.
        Users will not be allowed to login at all unless a role for them is found in OIDC if set to true

        :param auth_requires_role: The auth_requires_role of this OIDCConfig.
        :type: bool
        """

        self._auth_requires_role = auth_requires_role

    @property
    def user_attributes(self):
        """
        Gets the user_attributes of this OIDCConfig.
        (Read-only) Array of mappings between OIDC User Attributes and Looker User Attributes

        :return: The user_attributes of this OIDCConfig.
        :rtype: list[OIDCUserAttributeRead]
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes):
        """
        Sets the user_attributes of this OIDCConfig.
        (Read-only) Array of mappings between OIDC User Attributes and Looker User Attributes

        :param user_attributes: The user_attributes of this OIDCConfig.
        :type: list[OIDCUserAttributeRead]
        """

        self._user_attributes = user_attributes

    @property
    def user_attributes_with_ids(self):
        """
        Gets the user_attributes_with_ids of this OIDCConfig.
        (Read/Write) Array of mappings between OIDC User Attributes and arrays of Looker User Attribute ids

        :return: The user_attributes_with_ids of this OIDCConfig.
        :rtype: list[OIDCUserAttributeWrite]
        """
        return self._user_attributes_with_ids

    @user_attributes_with_ids.setter
    def user_attributes_with_ids(self, user_attributes_with_ids):
        """
        Sets the user_attributes_with_ids of this OIDCConfig.
        (Read/Write) Array of mappings between OIDC User Attributes and arrays of Looker User Attribute ids

        :param user_attributes_with_ids: The user_attributes_with_ids of this OIDCConfig.
        :type: list[OIDCUserAttributeWrite]
        """

        self._user_attributes_with_ids = user_attributes_with_ids

    @property
    def url(self):
        """
        Gets the url of this OIDCConfig.
        Link to get this item

        :return: The url of this OIDCConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OIDCConfig.
        Link to get this item

        :param url: The url of this OIDCConfig.
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """
        Gets the can of this OIDCConfig.
        Operations the current user is able to perform on this object

        :return: The can of this OIDCConfig.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this OIDCConfig.
        Operations the current user is able to perform on this object

        :param can: The can of this OIDCConfig.
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, OIDCConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
