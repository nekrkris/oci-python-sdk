# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .header_manipulation_action import HeaderManipulationAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveHttpResponseHeaderAction(HeaderManipulationAction):
    """
    An object that represents the action of removing from a response all occurrences of header fields
    with a specified name.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveHttpResponseHeaderAction object with values from keyword arguments. The default value of the :py:attr:`~oci.waas.models.RemoveHttpResponseHeaderAction.action` attribute
        of this class is ``REMOVE_HTTP_RESPONSE_HEADER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this RemoveHttpResponseHeaderAction.
            Allowed values for this property are: "EXTEND_HTTP_RESPONSE_HEADER", "ADD_HTTP_RESPONSE_HEADER", "REMOVE_HTTP_RESPONSE_HEADER"
        :type action: str

        :param header:
            The value to assign to the header property of this RemoveHttpResponseHeaderAction.
        :type header: str

        """
        self.swagger_types = {
            'action': 'str',
            'header': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'header': 'header'
        }

        self._action = None
        self._header = None
        self._action = 'REMOVE_HTTP_RESPONSE_HEADER'

    @property
    def header(self):
        """
        **[Required]** Gets the header of this RemoveHttpResponseHeaderAction.
        A header field name that conforms to RFC 7230.

        Example: `example_header_name`


        :return: The header of this RemoveHttpResponseHeaderAction.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this RemoveHttpResponseHeaderAction.
        A header field name that conforms to RFC 7230.

        Example: `example_header_name`


        :param header: The header of this RemoveHttpResponseHeaderAction.
        :type: str
        """
        self._header = header

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
