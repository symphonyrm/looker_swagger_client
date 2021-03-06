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


class ApiVersionElement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, version=None, full_version=None, status=None, swagger_url=None):
        """
        ApiVersionElement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'version': 'str',
            'full_version': 'str',
            'status': 'str',
            'swagger_url': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'full_version': 'full_version',
            'status': 'status',
            'swagger_url': 'swagger_url'
        }

        self._version = version
        self._full_version = full_version
        self._status = status
        self._swagger_url = swagger_url

    @property
    def version(self):
        """
        Gets the version of this ApiVersionElement.
        Version number as it appears in '/api/xxx/' urls

        :return: The version of this ApiVersionElement.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ApiVersionElement.
        Version number as it appears in '/api/xxx/' urls

        :param version: The version of this ApiVersionElement.
        :type: str
        """

        self._version = version

    @property
    def full_version(self):
        """
        Gets the full_version of this ApiVersionElement.
        Full version number including minor version

        :return: The full_version of this ApiVersionElement.
        :rtype: str
        """
        return self._full_version

    @full_version.setter
    def full_version(self, full_version):
        """
        Sets the full_version of this ApiVersionElement.
        Full version number including minor version

        :param full_version: The full_version of this ApiVersionElement.
        :type: str
        """

        self._full_version = full_version

    @property
    def status(self):
        """
        Gets the status of this ApiVersionElement.
        Status of this version

        :return: The status of this ApiVersionElement.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ApiVersionElement.
        Status of this version

        :param status: The status of this ApiVersionElement.
        :type: str
        """

        self._status = status

    @property
    def swagger_url(self):
        """
        Gets the swagger_url of this ApiVersionElement.
        Url for swagger.json for this version

        :return: The swagger_url of this ApiVersionElement.
        :rtype: str
        """
        return self._swagger_url

    @swagger_url.setter
    def swagger_url(self, swagger_url):
        """
        Sets the swagger_url of this ApiVersionElement.
        Url for swagger.json for this version

        :param swagger_url: The swagger_url of this ApiVersionElement.
        :type: str
        """

        self._swagger_url = swagger_url

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
        if not isinstance(other, ApiVersionElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
