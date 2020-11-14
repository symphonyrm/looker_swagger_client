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


class HomepageSection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, is_dynamic=None, is_header=None, order=None, detail_url=None, can=None):
        """
        HomepageSection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'is_dynamic': 'bool',
            'is_header': 'bool',
            'order': 'float',
            'detail_url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'is_dynamic': 'is_dynamic',
            'is_header': 'is_header',
            'order': 'order',
            'detail_url': 'detail_url',
            'can': 'can'
        }

        self._id = id
        self._title = title
        self._is_dynamic = is_dynamic
        self._is_header = is_header
        self._order = order
        self._detail_url = detail_url
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this HomepageSection.
        Unique Id

        :return: The id of this HomepageSection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HomepageSection.
        Unique Id

        :param id: The id of this HomepageSection.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this HomepageSection.
        Name of row

        :return: The title of this HomepageSection.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this HomepageSection.
        Name of row

        :param title: The title of this HomepageSection.
        :type: str
        """

        self._title = title

    @property
    def is_dynamic(self):
        """
        Gets the is_dynamic of this HomepageSection.
        This section was automatically generated by Looker

        :return: The is_dynamic of this HomepageSection.
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        """
        Sets the is_dynamic of this HomepageSection.
        This section was automatically generated by Looker

        :param is_dynamic: The is_dynamic of this HomepageSection.
        :type: bool
        """

        self._is_dynamic = is_dynamic

    @property
    def is_header(self):
        """
        Gets the is_header of this HomepageSection.
        Is this a header section (has no items)

        :return: The is_header of this HomepageSection.
        :rtype: bool
        """
        return self._is_header

    @is_header.setter
    def is_header(self, is_header):
        """
        Sets the is_header of this HomepageSection.
        Is this a header section (has no items)

        :param is_header: The is_header of this HomepageSection.
        :type: bool
        """

        self._is_header = is_header

    @property
    def order(self):
        """
        Gets the order of this HomepageSection.
        An arbitrary float representing the sort order of sections.

        :return: The order of this HomepageSection.
        :rtype: float
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this HomepageSection.
        An arbitrary float representing the sort order of sections.

        :param order: The order of this HomepageSection.
        :type: float
        """

        self._order = order

    @property
    def detail_url(self):
        """
        Gets the detail_url of this HomepageSection.
        A URL pointing to a page showing further information about the content in the section.

        :return: The detail_url of this HomepageSection.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """
        Sets the detail_url of this HomepageSection.
        A URL pointing to a page showing further information about the content in the section.

        :param detail_url: The detail_url of this HomepageSection.
        :type: str
        """

        self._detail_url = detail_url

    @property
    def can(self):
        """
        Gets the can of this HomepageSection.
        Operations the current user is able to perform on this object

        :return: The can of this HomepageSection.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this HomepageSection.
        Operations the current user is able to perform on this object

        :param can: The can of this HomepageSection.
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
        if not isinstance(other, HomepageSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
