# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ArchiverError(object):
    """
    An error related to a stream archiver.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ArchiverError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this ArchiverError.
        :type code: str

        :param message:
            The value to assign to the message property of this ArchiverError.
        :type message: str

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = None
        self._message = None

    @property
    def code(self):
        """
        Gets the code of this ArchiverError.
        A short error code that defines the error, meant for programmatic parsing.


        :return: The code of this ArchiverError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ArchiverError.
        A short error code that defines the error, meant for programmatic parsing.


        :param code: The code of this ArchiverError.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ArchiverError.
        A human-readable error string.


        :return: The message of this ArchiverError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ArchiverError.
        A human-readable error string.


        :param message: The message of this ArchiverError.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
