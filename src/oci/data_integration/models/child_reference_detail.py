# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChildReferenceDetail(object):
    """
    References used in an application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChildReferenceDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ChildReferenceDetail.
        :type key: str

        :param target_object:
            The value to assign to the target_object property of this ChildReferenceDetail.
        :type target_object: object

        """
        self.swagger_types = {
            'key': 'str',
            'target_object': 'object'
        }

        self.attribute_map = {
            'key': 'key',
            'target_object': 'targetObject'
        }

        self._key = None
        self._target_object = None

    @property
    def key(self):
        """
        Gets the key of this ChildReferenceDetail.
        The child reference key.


        :return: The key of this ChildReferenceDetail.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ChildReferenceDetail.
        The child reference key.


        :param key: The key of this ChildReferenceDetail.
        :type: str
        """
        self._key = key

    @property
    def target_object(self):
        """
        Gets the target_object of this ChildReferenceDetail.
        The new reference object to use instead of the original reference. For example, this can be a connection reference.


        :return: The target_object of this ChildReferenceDetail.
        :rtype: object
        """
        return self._target_object

    @target_object.setter
    def target_object(self, target_object):
        """
        Sets the target_object of this ChildReferenceDetail.
        The new reference object to use instead of the original reference. For example, this can be a connection reference.


        :param target_object: The target_object of this ChildReferenceDetail.
        :type: object
        """
        self._target_object = target_object

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
