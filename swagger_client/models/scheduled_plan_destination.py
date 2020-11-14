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


class ScheduledPlanDestination(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, scheduled_plan_id=None, format=None, apply_formatting=None, apply_vis=None, address=None, looker_recipient=None, type=None, parameters=None, secret_parameters=None, message=None, can=None):
        """
        ScheduledPlanDestination - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'scheduled_plan_id': 'int',
            'format': 'str',
            'apply_formatting': 'bool',
            'apply_vis': 'bool',
            'address': 'str',
            'looker_recipient': 'bool',
            'type': 'str',
            'parameters': 'str',
            'secret_parameters': 'str',
            'message': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'scheduled_plan_id': 'scheduled_plan_id',
            'format': 'format',
            'apply_formatting': 'apply_formatting',
            'apply_vis': 'apply_vis',
            'address': 'address',
            'looker_recipient': 'looker_recipient',
            'type': 'type',
            'parameters': 'parameters',
            'secret_parameters': 'secret_parameters',
            'message': 'message',
            'can': 'can'
        }

        self._id = id
        self._scheduled_plan_id = scheduled_plan_id
        self._format = format
        self._apply_formatting = apply_formatting
        self._apply_vis = apply_vis
        self._address = address
        self._looker_recipient = looker_recipient
        self._type = type
        self._parameters = parameters
        self._secret_parameters = secret_parameters
        self._message = message
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this ScheduledPlanDestination.
        Unique Id

        :return: The id of this ScheduledPlanDestination.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledPlanDestination.
        Unique Id

        :param id: The id of this ScheduledPlanDestination.
        :type: int
        """

        self._id = id

    @property
    def scheduled_plan_id(self):
        """
        Gets the scheduled_plan_id of this ScheduledPlanDestination.
        Id of a scheduled plan you own

        :return: The scheduled_plan_id of this ScheduledPlanDestination.
        :rtype: int
        """
        return self._scheduled_plan_id

    @scheduled_plan_id.setter
    def scheduled_plan_id(self, scheduled_plan_id):
        """
        Sets the scheduled_plan_id of this ScheduledPlanDestination.
        Id of a scheduled plan you own

        :param scheduled_plan_id: The scheduled_plan_id of this ScheduledPlanDestination.
        :type: int
        """

        self._scheduled_plan_id = scheduled_plan_id

    @property
    def format(self):
        """
        Gets the format of this ScheduledPlanDestination.
        Format requested by the given destination (i.e. PDF, etc.)

        :return: The format of this ScheduledPlanDestination.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this ScheduledPlanDestination.
        Format requested by the given destination (i.e. PDF, etc.)

        :param format: The format of this ScheduledPlanDestination.
        :type: str
        """

        self._format = format

    @property
    def apply_formatting(self):
        """
        Gets the apply_formatting of this ScheduledPlanDestination.
        Are values formatted? (containing currency symbols, digit separators, etc.

        :return: The apply_formatting of this ScheduledPlanDestination.
        :rtype: bool
        """
        return self._apply_formatting

    @apply_formatting.setter
    def apply_formatting(self, apply_formatting):
        """
        Sets the apply_formatting of this ScheduledPlanDestination.
        Are values formatted? (containing currency symbols, digit separators, etc.

        :param apply_formatting: The apply_formatting of this ScheduledPlanDestination.
        :type: bool
        """

        self._apply_formatting = apply_formatting

    @property
    def apply_vis(self):
        """
        Gets the apply_vis of this ScheduledPlanDestination.
        Whether visualization options are applied to the results.

        :return: The apply_vis of this ScheduledPlanDestination.
        :rtype: bool
        """
        return self._apply_vis

    @apply_vis.setter
    def apply_vis(self, apply_vis):
        """
        Sets the apply_vis of this ScheduledPlanDestination.
        Whether visualization options are applied to the results.

        :param apply_vis: The apply_vis of this ScheduledPlanDestination.
        :type: bool
        """

        self._apply_vis = apply_vis

    @property
    def address(self):
        """
        Gets the address of this ScheduledPlanDestination.
        Address for recipient. For email e.g. 'user@example.com'. For webhooks e.g. 'https://domain/path'. For Amazon S3 e.g. 's3://bucket-name/path/'. For SFTP e.g. 'sftp://host-name/path/'. 

        :return: The address of this ScheduledPlanDestination.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ScheduledPlanDestination.
        Address for recipient. For email e.g. 'user@example.com'. For webhooks e.g. 'https://domain/path'. For Amazon S3 e.g. 's3://bucket-name/path/'. For SFTP e.g. 'sftp://host-name/path/'. 

        :param address: The address of this ScheduledPlanDestination.
        :type: str
        """

        self._address = address

    @property
    def looker_recipient(self):
        """
        Gets the looker_recipient of this ScheduledPlanDestination.
        Whether the recipient is a Looker user on the current instance (only applicable for email recipients)

        :return: The looker_recipient of this ScheduledPlanDestination.
        :rtype: bool
        """
        return self._looker_recipient

    @looker_recipient.setter
    def looker_recipient(self, looker_recipient):
        """
        Sets the looker_recipient of this ScheduledPlanDestination.
        Whether the recipient is a Looker user on the current instance (only applicable for email recipients)

        :param looker_recipient: The looker_recipient of this ScheduledPlanDestination.
        :type: bool
        """

        self._looker_recipient = looker_recipient

    @property
    def type(self):
        """
        Gets the type of this ScheduledPlanDestination.
        Type of the address ('email', 'webhook', 's3', or 'sftp')

        :return: The type of this ScheduledPlanDestination.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ScheduledPlanDestination.
        Type of the address ('email', 'webhook', 's3', or 'sftp')

        :param type: The type of this ScheduledPlanDestination.
        :type: str
        """

        self._type = type

    @property
    def parameters(self):
        """
        Gets the parameters of this ScheduledPlanDestination.
        JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username.

        :return: The parameters of this ScheduledPlanDestination.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ScheduledPlanDestination.
        JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username.

        :param parameters: The parameters of this ScheduledPlanDestination.
        :type: str
        """

        self._parameters = parameters

    @property
    def secret_parameters(self):
        """
        Gets the secret_parameters of this ScheduledPlanDestination.
        (Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password.

        :return: The secret_parameters of this ScheduledPlanDestination.
        :rtype: str
        """
        return self._secret_parameters

    @secret_parameters.setter
    def secret_parameters(self, secret_parameters):
        """
        Sets the secret_parameters of this ScheduledPlanDestination.
        (Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password.

        :param secret_parameters: The secret_parameters of this ScheduledPlanDestination.
        :type: str
        """

        self._secret_parameters = secret_parameters

    @property
    def message(self):
        """
        Gets the message of this ScheduledPlanDestination.
        Optional message to be included in scheduled emails

        :return: The message of this ScheduledPlanDestination.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ScheduledPlanDestination.
        Optional message to be included in scheduled emails

        :param message: The message of this ScheduledPlanDestination.
        :type: str
        """

        self._message = message

    @property
    def can(self):
        """
        Gets the can of this ScheduledPlanDestination.
        Operations the current user is able to perform on this object

        :return: The can of this ScheduledPlanDestination.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this ScheduledPlanDestination.
        Operations the current user is able to perform on this object

        :param can: The can of this ScheduledPlanDestination.
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
        if not isinstance(other, ScheduledPlanDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other