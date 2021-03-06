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


class Dashboard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, content_metadata_id=None, content_favorite_id=None, view_count=None, last_accessed_at=None, favorite_count=None, user_id=None, title=None, description=None, readonly=None, hidden=None, refresh_interval=None, refresh_interval_to_i=None, space=None, load_configuration=None, model=None, space_id=None, dashboard_elements=None, dashboard_layouts=None, dashboard_filters=None, last_viewed_at=None, background_color=None, show_title=None, title_color=None, show_filters_bar=None, tile_background_color=None, tile_text_color=None, text_tile_text_color=None, last_updater_id=None, deleter_id=None, deleted=None, created_at=None, deleted_at=None, query_timezone=None, edit_uri=None, can=None):
        """
        Dashboard - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'content_metadata_id': 'int',
            'content_favorite_id': 'int',
            'view_count': 'int',
            'last_accessed_at': 'datetime',
            'favorite_count': 'int',
            'user_id': 'int',
            'title': 'str',
            'description': 'str',
            'readonly': 'bool',
            'hidden': 'bool',
            'refresh_interval': 'str',
            'refresh_interval_to_i': 'int',
            'space': 'SpaceBase',
            'load_configuration': 'str',
            'model': 'LookModel',
            'space_id': 'str',
            'dashboard_elements': 'list[DashboardElement]',
            'dashboard_layouts': 'list[DashboardLayout]',
            'dashboard_filters': 'list[DashboardFilter]',
            'last_viewed_at': 'datetime',
            'background_color': 'str',
            'show_title': 'bool',
            'title_color': 'str',
            'show_filters_bar': 'bool',
            'tile_background_color': 'str',
            'tile_text_color': 'str',
            'text_tile_text_color': 'str',
            'last_updater_id': 'int',
            'deleter_id': 'int',
            'deleted': 'bool',
            'created_at': 'datetime',
            'deleted_at': 'datetime',
            'query_timezone': 'str',
            'edit_uri': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'content_metadata_id': 'content_metadata_id',
            'content_favorite_id': 'content_favorite_id',
            'view_count': 'view_count',
            'last_accessed_at': 'last_accessed_at',
            'favorite_count': 'favorite_count',
            'user_id': 'user_id',
            'title': 'title',
            'description': 'description',
            'readonly': 'readonly',
            'hidden': 'hidden',
            'refresh_interval': 'refresh_interval',
            'refresh_interval_to_i': 'refresh_interval_to_i',
            'space': 'space',
            'load_configuration': 'load_configuration',
            'model': 'model',
            'space_id': 'space_id',
            'dashboard_elements': 'dashboard_elements',
            'dashboard_layouts': 'dashboard_layouts',
            'dashboard_filters': 'dashboard_filters',
            'last_viewed_at': 'last_viewed_at',
            'background_color': 'background_color',
            'show_title': 'show_title',
            'title_color': 'title_color',
            'show_filters_bar': 'show_filters_bar',
            'tile_background_color': 'tile_background_color',
            'tile_text_color': 'tile_text_color',
            'text_tile_text_color': 'text_tile_text_color',
            'last_updater_id': 'last_updater_id',
            'deleter_id': 'deleter_id',
            'deleted': 'deleted',
            'created_at': 'created_at',
            'deleted_at': 'deleted_at',
            'query_timezone': 'query_timezone',
            'edit_uri': 'edit_uri',
            'can': 'can'
        }

        self._id = id
        self._content_metadata_id = content_metadata_id
        self._content_favorite_id = content_favorite_id
        self._view_count = view_count
        self._last_accessed_at = last_accessed_at
        self._favorite_count = favorite_count
        self._user_id = user_id
        self._title = title
        self._description = description
        self._readonly = readonly
        self._hidden = hidden
        self._refresh_interval = refresh_interval
        self._refresh_interval_to_i = refresh_interval_to_i
        self._space = space
        self._load_configuration = load_configuration
        self._model = model
        self._space_id = space_id
        self._dashboard_elements = dashboard_elements
        self._dashboard_layouts = dashboard_layouts
        self._dashboard_filters = dashboard_filters
        self._last_viewed_at = last_viewed_at
        self._background_color = background_color
        self._show_title = show_title
        self._title_color = title_color
        self._show_filters_bar = show_filters_bar
        self._tile_background_color = tile_background_color
        self._tile_text_color = tile_text_color
        self._text_tile_text_color = text_tile_text_color
        self._last_updater_id = last_updater_id
        self._deleter_id = deleter_id
        self._deleted = deleted
        self._created_at = created_at
        self._deleted_at = deleted_at
        self._query_timezone = query_timezone
        self._edit_uri = edit_uri
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this Dashboard.
        Unique Id

        :return: The id of this Dashboard.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Dashboard.
        Unique Id

        :param id: The id of this Dashboard.
        :type: str
        """

        self._id = id

    @property
    def content_metadata_id(self):
        """
        Gets the content_metadata_id of this Dashboard.
        Id of content metadata

        :return: The content_metadata_id of this Dashboard.
        :rtype: int
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """
        Sets the content_metadata_id of this Dashboard.
        Id of content metadata

        :param content_metadata_id: The content_metadata_id of this Dashboard.
        :type: int
        """

        self._content_metadata_id = content_metadata_id

    @property
    def content_favorite_id(self):
        """
        Gets the content_favorite_id of this Dashboard.
        Content Favorite Id

        :return: The content_favorite_id of this Dashboard.
        :rtype: int
        """
        return self._content_favorite_id

    @content_favorite_id.setter
    def content_favorite_id(self, content_favorite_id):
        """
        Sets the content_favorite_id of this Dashboard.
        Content Favorite Id

        :param content_favorite_id: The content_favorite_id of this Dashboard.
        :type: int
        """

        self._content_favorite_id = content_favorite_id

    @property
    def view_count(self):
        """
        Gets the view_count of this Dashboard.
        Number of times viewed in the Looker web UI

        :return: The view_count of this Dashboard.
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """
        Sets the view_count of this Dashboard.
        Number of times viewed in the Looker web UI

        :param view_count: The view_count of this Dashboard.
        :type: int
        """

        self._view_count = view_count

    @property
    def last_accessed_at(self):
        """
        Gets the last_accessed_at of this Dashboard.
        Time the dashboard was last accessed

        :return: The last_accessed_at of this Dashboard.
        :rtype: datetime
        """
        return self._last_accessed_at

    @last_accessed_at.setter
    def last_accessed_at(self, last_accessed_at):
        """
        Sets the last_accessed_at of this Dashboard.
        Time the dashboard was last accessed

        :param last_accessed_at: The last_accessed_at of this Dashboard.
        :type: datetime
        """

        self._last_accessed_at = last_accessed_at

    @property
    def favorite_count(self):
        """
        Gets the favorite_count of this Dashboard.
        Number of times favorited

        :return: The favorite_count of this Dashboard.
        :rtype: int
        """
        return self._favorite_count

    @favorite_count.setter
    def favorite_count(self, favorite_count):
        """
        Sets the favorite_count of this Dashboard.
        Number of times favorited

        :param favorite_count: The favorite_count of this Dashboard.
        :type: int
        """

        self._favorite_count = favorite_count

    @property
    def user_id(self):
        """
        Gets the user_id of this Dashboard.
        Id of User

        :return: The user_id of this Dashboard.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Dashboard.
        Id of User

        :param user_id: The user_id of this Dashboard.
        :type: int
        """

        self._user_id = user_id

    @property
    def title(self):
        """
        Gets the title of this Dashboard.
        Look Title

        :return: The title of this Dashboard.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Dashboard.
        Look Title

        :param title: The title of this Dashboard.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this Dashboard.
        Description

        :return: The description of this Dashboard.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Dashboard.
        Description

        :param description: The description of this Dashboard.
        :type: str
        """

        self._description = description

    @property
    def readonly(self):
        """
        Gets the readonly of this Dashboard.
        Is Read-only

        :return: The readonly of this Dashboard.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """
        Sets the readonly of this Dashboard.
        Is Read-only

        :param readonly: The readonly of this Dashboard.
        :type: bool
        """

        self._readonly = readonly

    @property
    def hidden(self):
        """
        Gets the hidden of this Dashboard.
        Is Hidden

        :return: The hidden of this Dashboard.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """
        Sets the hidden of this Dashboard.
        Is Hidden

        :param hidden: The hidden of this Dashboard.
        :type: bool
        """

        self._hidden = hidden

    @property
    def refresh_interval(self):
        """
        Gets the refresh_interval of this Dashboard.
        Refresh Interval

        :return: The refresh_interval of this Dashboard.
        :rtype: str
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """
        Sets the refresh_interval of this Dashboard.
        Refresh Interval

        :param refresh_interval: The refresh_interval of this Dashboard.
        :type: str
        """

        self._refresh_interval = refresh_interval

    @property
    def refresh_interval_to_i(self):
        """
        Gets the refresh_interval_to_i of this Dashboard.
        Refresh Interval as Integer

        :return: The refresh_interval_to_i of this Dashboard.
        :rtype: int
        """
        return self._refresh_interval_to_i

    @refresh_interval_to_i.setter
    def refresh_interval_to_i(self, refresh_interval_to_i):
        """
        Sets the refresh_interval_to_i of this Dashboard.
        Refresh Interval as Integer

        :param refresh_interval_to_i: The refresh_interval_to_i of this Dashboard.
        :type: int
        """

        self._refresh_interval_to_i = refresh_interval_to_i

    @property
    def space(self):
        """
        Gets the space of this Dashboard.
        Space

        :return: The space of this Dashboard.
        :rtype: SpaceBase
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this Dashboard.
        Space

        :param space: The space of this Dashboard.
        :type: SpaceBase
        """

        self._space = space

    @property
    def load_configuration(self):
        """
        Gets the load_configuration of this Dashboard.
        configuration option that governs how dashboard loading will happen.

        :return: The load_configuration of this Dashboard.
        :rtype: str
        """
        return self._load_configuration

    @load_configuration.setter
    def load_configuration(self, load_configuration):
        """
        Sets the load_configuration of this Dashboard.
        configuration option that governs how dashboard loading will happen.

        :param load_configuration: The load_configuration of this Dashboard.
        :type: str
        """

        self._load_configuration = load_configuration

    @property
    def model(self):
        """
        Gets the model of this Dashboard.
        Model

        :return: The model of this Dashboard.
        :rtype: LookModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Dashboard.
        Model

        :param model: The model of this Dashboard.
        :type: LookModel
        """

        self._model = model

    @property
    def space_id(self):
        """
        Gets the space_id of this Dashboard.
        Id of Space

        :return: The space_id of this Dashboard.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """
        Sets the space_id of this Dashboard.
        Id of Space

        :param space_id: The space_id of this Dashboard.
        :type: str
        """

        self._space_id = space_id

    @property
    def dashboard_elements(self):
        """
        Gets the dashboard_elements of this Dashboard.
        Elements

        :return: The dashboard_elements of this Dashboard.
        :rtype: list[DashboardElement]
        """
        return self._dashboard_elements

    @dashboard_elements.setter
    def dashboard_elements(self, dashboard_elements):
        """
        Sets the dashboard_elements of this Dashboard.
        Elements

        :param dashboard_elements: The dashboard_elements of this Dashboard.
        :type: list[DashboardElement]
        """

        self._dashboard_elements = dashboard_elements

    @property
    def dashboard_layouts(self):
        """
        Gets the dashboard_layouts of this Dashboard.
        Layouts

        :return: The dashboard_layouts of this Dashboard.
        :rtype: list[DashboardLayout]
        """
        return self._dashboard_layouts

    @dashboard_layouts.setter
    def dashboard_layouts(self, dashboard_layouts):
        """
        Sets the dashboard_layouts of this Dashboard.
        Layouts

        :param dashboard_layouts: The dashboard_layouts of this Dashboard.
        :type: list[DashboardLayout]
        """

        self._dashboard_layouts = dashboard_layouts

    @property
    def dashboard_filters(self):
        """
        Gets the dashboard_filters of this Dashboard.
        Filters

        :return: The dashboard_filters of this Dashboard.
        :rtype: list[DashboardFilter]
        """
        return self._dashboard_filters

    @dashboard_filters.setter
    def dashboard_filters(self, dashboard_filters):
        """
        Sets the dashboard_filters of this Dashboard.
        Filters

        :param dashboard_filters: The dashboard_filters of this Dashboard.
        :type: list[DashboardFilter]
        """

        self._dashboard_filters = dashboard_filters

    @property
    def last_viewed_at(self):
        """
        Gets the last_viewed_at of this Dashboard.
        Time last viewed in the Looker web UI

        :return: The last_viewed_at of this Dashboard.
        :rtype: datetime
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(self, last_viewed_at):
        """
        Sets the last_viewed_at of this Dashboard.
        Time last viewed in the Looker web UI

        :param last_viewed_at: The last_viewed_at of this Dashboard.
        :type: datetime
        """

        self._last_viewed_at = last_viewed_at

    @property
    def background_color(self):
        """
        Gets the background_color of this Dashboard.
        Background color

        :return: The background_color of this Dashboard.
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this Dashboard.
        Background color

        :param background_color: The background_color of this Dashboard.
        :type: str
        """

        self._background_color = background_color

    @property
    def show_title(self):
        """
        Gets the show_title of this Dashboard.
        Show title

        :return: The show_title of this Dashboard.
        :rtype: bool
        """
        return self._show_title

    @show_title.setter
    def show_title(self, show_title):
        """
        Sets the show_title of this Dashboard.
        Show title

        :param show_title: The show_title of this Dashboard.
        :type: bool
        """

        self._show_title = show_title

    @property
    def title_color(self):
        """
        Gets the title_color of this Dashboard.
        Title color

        :return: The title_color of this Dashboard.
        :rtype: str
        """
        return self._title_color

    @title_color.setter
    def title_color(self, title_color):
        """
        Sets the title_color of this Dashboard.
        Title color

        :param title_color: The title_color of this Dashboard.
        :type: str
        """

        self._title_color = title_color

    @property
    def show_filters_bar(self):
        """
        Gets the show_filters_bar of this Dashboard.
        Show filters bar.  **Security Note:** This property only affects the *cosmetic* appearance of the dashboard, not a user'Ls ability to access data. Hiding the filters bar does **NOT** prevent users from changing filters by other means. For information on how to set up secure data access control policies, see [Control User Access to Data](https://docs.looker.com/admin-options/tutorials/permissions#control_user_access_to_data)

        :return: The show_filters_bar of this Dashboard.
        :rtype: bool
        """
        return self._show_filters_bar

    @show_filters_bar.setter
    def show_filters_bar(self, show_filters_bar):
        """
        Sets the show_filters_bar of this Dashboard.
        Show filters bar.  **Security Note:** This property only affects the *cosmetic* appearance of the dashboard, not a user'Ls ability to access data. Hiding the filters bar does **NOT** prevent users from changing filters by other means. For information on how to set up secure data access control policies, see [Control User Access to Data](https://docs.looker.com/admin-options/tutorials/permissions#control_user_access_to_data)

        :param show_filters_bar: The show_filters_bar of this Dashboard.
        :type: bool
        """

        self._show_filters_bar = show_filters_bar

    @property
    def tile_background_color(self):
        """
        Gets the tile_background_color of this Dashboard.
        Tile background color

        :return: The tile_background_color of this Dashboard.
        :rtype: str
        """
        return self._tile_background_color

    @tile_background_color.setter
    def tile_background_color(self, tile_background_color):
        """
        Sets the tile_background_color of this Dashboard.
        Tile background color

        :param tile_background_color: The tile_background_color of this Dashboard.
        :type: str
        """

        self._tile_background_color = tile_background_color

    @property
    def tile_text_color(self):
        """
        Gets the tile_text_color of this Dashboard.
        Tile text color

        :return: The tile_text_color of this Dashboard.
        :rtype: str
        """
        return self._tile_text_color

    @tile_text_color.setter
    def tile_text_color(self, tile_text_color):
        """
        Sets the tile_text_color of this Dashboard.
        Tile text color

        :param tile_text_color: The tile_text_color of this Dashboard.
        :type: str
        """

        self._tile_text_color = tile_text_color

    @property
    def text_tile_text_color(self):
        """
        Gets the text_tile_text_color of this Dashboard.
        Color of text on text tiles

        :return: The text_tile_text_color of this Dashboard.
        :rtype: str
        """
        return self._text_tile_text_color

    @text_tile_text_color.setter
    def text_tile_text_color(self, text_tile_text_color):
        """
        Sets the text_tile_text_color of this Dashboard.
        Color of text on text tiles

        :param text_tile_text_color: The text_tile_text_color of this Dashboard.
        :type: str
        """

        self._text_tile_text_color = text_tile_text_color

    @property
    def last_updater_id(self):
        """
        Gets the last_updater_id of this Dashboard.
        Id of User that last updated the dashboard.

        :return: The last_updater_id of this Dashboard.
        :rtype: int
        """
        return self._last_updater_id

    @last_updater_id.setter
    def last_updater_id(self, last_updater_id):
        """
        Sets the last_updater_id of this Dashboard.
        Id of User that last updated the dashboard.

        :param last_updater_id: The last_updater_id of this Dashboard.
        :type: int
        """

        self._last_updater_id = last_updater_id

    @property
    def deleter_id(self):
        """
        Gets the deleter_id of this Dashboard.
        Id of User that deleted the dashboard.

        :return: The deleter_id of this Dashboard.
        :rtype: int
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """
        Sets the deleter_id of this Dashboard.
        Id of User that deleted the dashboard.

        :param deleter_id: The deleter_id of this Dashboard.
        :type: int
        """

        self._deleter_id = deleter_id

    @property
    def deleted(self):
        """
        Gets the deleted of this Dashboard.
        Whether or not a dashboard is deleted.

        :return: The deleted of this Dashboard.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this Dashboard.
        Whether or not a dashboard is deleted.

        :param deleted: The deleted of this Dashboard.
        :type: bool
        """

        self._deleted = deleted

    @property
    def created_at(self):
        """
        Gets the created_at of this Dashboard.
        Time that the Dashboard was created.

        :return: The created_at of this Dashboard.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Dashboard.
        Time that the Dashboard was created.

        :param created_at: The created_at of this Dashboard.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this Dashboard.
        Time that the Dashboard was deleted.

        :return: The deleted_at of this Dashboard.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this Dashboard.
        Time that the Dashboard was deleted.

        :param deleted_at: The deleted_at of this Dashboard.
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def query_timezone(self):
        """
        Gets the query_timezone of this Dashboard.
        Timezone in which the Dashboard will run by default.

        :return: The query_timezone of this Dashboard.
        :rtype: str
        """
        return self._query_timezone

    @query_timezone.setter
    def query_timezone(self, query_timezone):
        """
        Sets the query_timezone of this Dashboard.
        Timezone in which the Dashboard will run by default.

        :param query_timezone: The query_timezone of this Dashboard.
        :type: str
        """

        self._query_timezone = query_timezone

    @property
    def edit_uri(self):
        """
        Gets the edit_uri of this Dashboard.
        Relative path of URI of LookML file to edit the dashboard (LookML dashboard only).

        :return: The edit_uri of this Dashboard.
        :rtype: str
        """
        return self._edit_uri

    @edit_uri.setter
    def edit_uri(self, edit_uri):
        """
        Sets the edit_uri of this Dashboard.
        Relative path of URI of LookML file to edit the dashboard (LookML dashboard only).

        :param edit_uri: The edit_uri of this Dashboard.
        :type: str
        """

        self._edit_uri = edit_uri

    @property
    def can(self):
        """
        Gets the can of this Dashboard.
        Operations the current user is able to perform on this object

        :return: The can of this Dashboard.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Dashboard.
        Operations the current user is able to perform on this object

        :param can: The can of this Dashboard.
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
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
