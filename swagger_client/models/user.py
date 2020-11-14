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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, first_name=None, last_name=None, display_name=None, email=None, is_disabled=None, avatar_url=None, home_space_id=None, personal_space_id=None, embed_group_space_id=None, access_filters=None, credentials_email=None, credentials_totp=None, credentials_ldap=None, credentials_google=None, credentials_saml=None, credentials_oidc=None, credentials_api=None, credentials_api3=None, credentials_embed=None, credentials_looker_openid=None, sessions=None, role_ids=None, group_ids=None, presumed_looker_employee=None, verified_looker_employee=None, looker_versions=None, ui_state=None, locale=None, url=None, can=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'first_name': 'str',
            'last_name': 'str',
            'display_name': 'str',
            'email': 'str',
            'is_disabled': 'bool',
            'avatar_url': 'str',
            'home_space_id': 'str',
            'personal_space_id': 'int',
            'embed_group_space_id': 'int',
            'access_filters': 'list[AccessFilter]',
            'credentials_email': 'CredentialsEmail',
            'credentials_totp': 'CredentialsTotp',
            'credentials_ldap': 'CredentialsLDAP',
            'credentials_google': 'CredentialsGoogle',
            'credentials_saml': 'CredentialsSaml',
            'credentials_oidc': 'CredentialsOIDC',
            'credentials_api': 'CredentialsApi',
            'credentials_api3': 'list[CredentialsApi3]',
            'credentials_embed': 'list[CredentialsEmbed]',
            'credentials_looker_openid': 'CredentialsLookerOpenid',
            'sessions': 'list[Session]',
            'role_ids': 'list[int]',
            'group_ids': 'list[int]',
            'presumed_looker_employee': 'bool',
            'verified_looker_employee': 'bool',
            'looker_versions': 'list[str]',
            'ui_state': 'dict(str, str)',
            'locale': 'str',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'display_name': 'display_name',
            'email': 'email',
            'is_disabled': 'is_disabled',
            'avatar_url': 'avatar_url',
            'home_space_id': 'home_space_id',
            'personal_space_id': 'personal_space_id',
            'embed_group_space_id': 'embed_group_space_id',
            'access_filters': 'access_filters',
            'credentials_email': 'credentials_email',
            'credentials_totp': 'credentials_totp',
            'credentials_ldap': 'credentials_ldap',
            'credentials_google': 'credentials_google',
            'credentials_saml': 'credentials_saml',
            'credentials_oidc': 'credentials_oidc',
            'credentials_api': 'credentials_api',
            'credentials_api3': 'credentials_api3',
            'credentials_embed': 'credentials_embed',
            'credentials_looker_openid': 'credentials_looker_openid',
            'sessions': 'sessions',
            'role_ids': 'role_ids',
            'group_ids': 'group_ids',
            'presumed_looker_employee': 'presumed_looker_employee',
            'verified_looker_employee': 'verified_looker_employee',
            'looker_versions': 'looker_versions',
            'ui_state': 'ui_state',
            'locale': 'locale',
            'url': 'url',
            'can': 'can'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._display_name = display_name
        self._email = email
        self._is_disabled = is_disabled
        self._avatar_url = avatar_url
        self._home_space_id = home_space_id
        self._personal_space_id = personal_space_id
        self._embed_group_space_id = embed_group_space_id
        self._access_filters = access_filters
        self._credentials_email = credentials_email
        self._credentials_totp = credentials_totp
        self._credentials_ldap = credentials_ldap
        self._credentials_google = credentials_google
        self._credentials_saml = credentials_saml
        self._credentials_oidc = credentials_oidc
        self._credentials_api = credentials_api
        self._credentials_api3 = credentials_api3
        self._credentials_embed = credentials_embed
        self._credentials_looker_openid = credentials_looker_openid
        self._sessions = sessions
        self._role_ids = role_ids
        self._group_ids = group_ids
        self._presumed_looker_employee = presumed_looker_employee
        self._verified_looker_employee = verified_looker_employee
        self._looker_versions = looker_versions
        self._ui_state = ui_state
        self._locale = locale
        self._url = url
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this User.
        Unique Id

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        Unique Id

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """
        Gets the first_name of this User.
        First name

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.
        First name

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this User.
        Last name

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.
        Last name

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def display_name(self):
        """
        Gets the display_name of this User.
        Full name for display (available only if both first_name and last_name are set)

        :return: The display_name of this User.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this User.
        Full name for display (available only if both first_name and last_name are set)

        :param display_name: The display_name of this User.
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """
        Gets the email of this User.
        EMail address

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        EMail address

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this User.
        Account has been disabled

        :return: The is_disabled of this User.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this User.
        Account has been disabled

        :param is_disabled: The is_disabled of this User.
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this User.
        URL for the avatar image (may be generic)

        :return: The avatar_url of this User.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this User.
        URL for the avatar image (may be generic)

        :param avatar_url: The avatar_url of this User.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def home_space_id(self):
        """
        Gets the home_space_id of this User.
        ID string for user's home space

        :return: The home_space_id of this User.
        :rtype: str
        """
        return self._home_space_id

    @home_space_id.setter
    def home_space_id(self, home_space_id):
        """
        Sets the home_space_id of this User.
        ID string for user's home space

        :param home_space_id: The home_space_id of this User.
        :type: str
        """

        self._home_space_id = home_space_id

    @property
    def personal_space_id(self):
        """
        Gets the personal_space_id of this User.
        ID of user's personal space

        :return: The personal_space_id of this User.
        :rtype: int
        """
        return self._personal_space_id

    @personal_space_id.setter
    def personal_space_id(self, personal_space_id):
        """
        Sets the personal_space_id of this User.
        ID of user's personal space

        :param personal_space_id: The personal_space_id of this User.
        :type: int
        """

        self._personal_space_id = personal_space_id

    @property
    def embed_group_space_id(self):
        """
        Gets the embed_group_space_id of this User.
        (Embed only) ID of user's group space based on the external_group_id optionally specified during embed user login

        :return: The embed_group_space_id of this User.
        :rtype: int
        """
        return self._embed_group_space_id

    @embed_group_space_id.setter
    def embed_group_space_id(self, embed_group_space_id):
        """
        Sets the embed_group_space_id of this User.
        (Embed only) ID of user's group space based on the external_group_id optionally specified during embed user login

        :param embed_group_space_id: The embed_group_space_id of this User.
        :type: int
        """

        self._embed_group_space_id = embed_group_space_id

    @property
    def access_filters(self):
        """
        Gets the access_filters of this User.
        Model access filters.

        :return: The access_filters of this User.
        :rtype: list[AccessFilter]
        """
        return self._access_filters

    @access_filters.setter
    def access_filters(self, access_filters):
        """
        Sets the access_filters of this User.
        Model access filters.

        :param access_filters: The access_filters of this User.
        :type: list[AccessFilter]
        """

        self._access_filters = access_filters

    @property
    def credentials_email(self):
        """
        Gets the credentials_email of this User.
        Email/Password login credentials

        :return: The credentials_email of this User.
        :rtype: CredentialsEmail
        """
        return self._credentials_email

    @credentials_email.setter
    def credentials_email(self, credentials_email):
        """
        Sets the credentials_email of this User.
        Email/Password login credentials

        :param credentials_email: The credentials_email of this User.
        :type: CredentialsEmail
        """

        self._credentials_email = credentials_email

    @property
    def credentials_totp(self):
        """
        Gets the credentials_totp of this User.
        Two-factor credentials

        :return: The credentials_totp of this User.
        :rtype: CredentialsTotp
        """
        return self._credentials_totp

    @credentials_totp.setter
    def credentials_totp(self, credentials_totp):
        """
        Sets the credentials_totp of this User.
        Two-factor credentials

        :param credentials_totp: The credentials_totp of this User.
        :type: CredentialsTotp
        """

        self._credentials_totp = credentials_totp

    @property
    def credentials_ldap(self):
        """
        Gets the credentials_ldap of this User.
        LDAP credentials

        :return: The credentials_ldap of this User.
        :rtype: CredentialsLDAP
        """
        return self._credentials_ldap

    @credentials_ldap.setter
    def credentials_ldap(self, credentials_ldap):
        """
        Sets the credentials_ldap of this User.
        LDAP credentials

        :param credentials_ldap: The credentials_ldap of this User.
        :type: CredentialsLDAP
        """

        self._credentials_ldap = credentials_ldap

    @property
    def credentials_google(self):
        """
        Gets the credentials_google of this User.
        Google auth credentials

        :return: The credentials_google of this User.
        :rtype: CredentialsGoogle
        """
        return self._credentials_google

    @credentials_google.setter
    def credentials_google(self, credentials_google):
        """
        Sets the credentials_google of this User.
        Google auth credentials

        :param credentials_google: The credentials_google of this User.
        :type: CredentialsGoogle
        """

        self._credentials_google = credentials_google

    @property
    def credentials_saml(self):
        """
        Gets the credentials_saml of this User.
        Saml auth credentials

        :return: The credentials_saml of this User.
        :rtype: CredentialsSaml
        """
        return self._credentials_saml

    @credentials_saml.setter
    def credentials_saml(self, credentials_saml):
        """
        Sets the credentials_saml of this User.
        Saml auth credentials

        :param credentials_saml: The credentials_saml of this User.
        :type: CredentialsSaml
        """

        self._credentials_saml = credentials_saml

    @property
    def credentials_oidc(self):
        """
        Gets the credentials_oidc of this User.
        OpenID Connect auth credentials

        :return: The credentials_oidc of this User.
        :rtype: CredentialsOIDC
        """
        return self._credentials_oidc

    @credentials_oidc.setter
    def credentials_oidc(self, credentials_oidc):
        """
        Sets the credentials_oidc of this User.
        OpenID Connect auth credentials

        :param credentials_oidc: The credentials_oidc of this User.
        :type: CredentialsOIDC
        """

        self._credentials_oidc = credentials_oidc

    @property
    def credentials_api(self):
        """
        Gets the credentials_api of this User.
        API user credentials. NO LONGER SUPPORTED.

        :return: The credentials_api of this User.
        :rtype: CredentialsApi
        """
        return self._credentials_api

    @credentials_api.setter
    def credentials_api(self, credentials_api):
        """
        Sets the credentials_api of this User.
        API user credentials. NO LONGER SUPPORTED.

        :param credentials_api: The credentials_api of this User.
        :type: CredentialsApi
        """

        self._credentials_api = credentials_api

    @property
    def credentials_api3(self):
        """
        Gets the credentials_api3 of this User.
        API 3 credentials

        :return: The credentials_api3 of this User.
        :rtype: list[CredentialsApi3]
        """
        return self._credentials_api3

    @credentials_api3.setter
    def credentials_api3(self, credentials_api3):
        """
        Sets the credentials_api3 of this User.
        API 3 credentials

        :param credentials_api3: The credentials_api3 of this User.
        :type: list[CredentialsApi3]
        """

        self._credentials_api3 = credentials_api3

    @property
    def credentials_embed(self):
        """
        Gets the credentials_embed of this User.
        Embed credentials

        :return: The credentials_embed of this User.
        :rtype: list[CredentialsEmbed]
        """
        return self._credentials_embed

    @credentials_embed.setter
    def credentials_embed(self, credentials_embed):
        """
        Sets the credentials_embed of this User.
        Embed credentials

        :param credentials_embed: The credentials_embed of this User.
        :type: list[CredentialsEmbed]
        """

        self._credentials_embed = credentials_embed

    @property
    def credentials_looker_openid(self):
        """
        Gets the credentials_looker_openid of this User.
        LookerOpenID credentials. Used for login by Looker Analysts

        :return: The credentials_looker_openid of this User.
        :rtype: CredentialsLookerOpenid
        """
        return self._credentials_looker_openid

    @credentials_looker_openid.setter
    def credentials_looker_openid(self, credentials_looker_openid):
        """
        Sets the credentials_looker_openid of this User.
        LookerOpenID credentials. Used for login by Looker Analysts

        :param credentials_looker_openid: The credentials_looker_openid of this User.
        :type: CredentialsLookerOpenid
        """

        self._credentials_looker_openid = credentials_looker_openid

    @property
    def sessions(self):
        """
        Gets the sessions of this User.
        Active sessions

        :return: The sessions of this User.
        :rtype: list[Session]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """
        Sets the sessions of this User.
        Active sessions

        :param sessions: The sessions of this User.
        :type: list[Session]
        """

        self._sessions = sessions

    @property
    def role_ids(self):
        """
        Gets the role_ids of this User.
        Array of ids of the roles for this user

        :return: The role_ids of this User.
        :rtype: list[int]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """
        Sets the role_ids of this User.
        Array of ids of the roles for this user

        :param role_ids: The role_ids of this User.
        :type: list[int]
        """

        self._role_ids = role_ids

    @property
    def group_ids(self):
        """
        Gets the group_ids of this User.
        Array of ids of the groups for this user

        :return: The group_ids of this User.
        :rtype: list[int]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """
        Sets the group_ids of this User.
        Array of ids of the groups for this user

        :param group_ids: The group_ids of this User.
        :type: list[int]
        """

        self._group_ids = group_ids

    @property
    def presumed_looker_employee(self):
        """
        Gets the presumed_looker_employee of this User.
        User is identified as an employee of Looker

        :return: The presumed_looker_employee of this User.
        :rtype: bool
        """
        return self._presumed_looker_employee

    @presumed_looker_employee.setter
    def presumed_looker_employee(self, presumed_looker_employee):
        """
        Sets the presumed_looker_employee of this User.
        User is identified as an employee of Looker

        :param presumed_looker_employee: The presumed_looker_employee of this User.
        :type: bool
        """

        self._presumed_looker_employee = presumed_looker_employee

    @property
    def verified_looker_employee(self):
        """
        Gets the verified_looker_employee of this User.
        User is identified as an employee of Looker who has been verified via Looker corporate authentication

        :return: The verified_looker_employee of this User.
        :rtype: bool
        """
        return self._verified_looker_employee

    @verified_looker_employee.setter
    def verified_looker_employee(self, verified_looker_employee):
        """
        Sets the verified_looker_employee of this User.
        User is identified as an employee of Looker who has been verified via Looker corporate authentication

        :param verified_looker_employee: The verified_looker_employee of this User.
        :type: bool
        """

        self._verified_looker_employee = verified_looker_employee

    @property
    def looker_versions(self):
        """
        Gets the looker_versions of this User.
        Array of strings representing the Looker versions that this user has used (this only goes back as far as '3.54.0')

        :return: The looker_versions of this User.
        :rtype: list[str]
        """
        return self._looker_versions

    @looker_versions.setter
    def looker_versions(self, looker_versions):
        """
        Sets the looker_versions of this User.
        Array of strings representing the Looker versions that this user has used (this only goes back as far as '3.54.0')

        :param looker_versions: The looker_versions of this User.
        :type: list[str]
        """

        self._looker_versions = looker_versions

    @property
    def ui_state(self):
        """
        Gets the ui_state of this User.
        Per user dictionary of undocumented state information owned by the Looker UI.

        :return: The ui_state of this User.
        :rtype: dict(str, str)
        """
        return self._ui_state

    @ui_state.setter
    def ui_state(self, ui_state):
        """
        Sets the ui_state of this User.
        Per user dictionary of undocumented state information owned by the Looker UI.

        :param ui_state: The ui_state of this User.
        :type: dict(str, str)
        """

        self._ui_state = ui_state

    @property
    def locale(self):
        """
        Gets the locale of this User.
        User's preferred locale. User locale takes precedence over Looker's system-wide default locale. Locale determines language of display strings and date and numeric formatting in API responses. Locale string must be a 2 letter language code or a combination of language code and region code: 'en' or 'en-US', for example.

        :return: The locale of this User.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this User.
        User's preferred locale. User locale takes precedence over Looker's system-wide default locale. Locale determines language of display strings and date and numeric formatting in API responses. Locale string must be a 2 letter language code or a combination of language code and region code: 'en' or 'en-US', for example.

        :param locale: The locale of this User.
        :type: str
        """

        self._locale = locale

    @property
    def url(self):
        """
        Gets the url of this User.
        Link to get this item

        :return: The url of this User.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this User.
        Link to get this item

        :param url: The url of this User.
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """
        Gets the can of this User.
        Operations the current user is able to perform on this object

        :return: The can of this User.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this User.
        Operations the current user is able to perform on this object

        :param can: The can of this User.
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
