# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStreamDetails(object):
    """
    Object used to update a stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStreamDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stream_pool_id:
            The value to assign to the stream_pool_id property of this UpdateStreamDetails.
        :type stream_pool_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateStreamDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateStreamDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'stream_pool_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'stream_pool_id': 'streamPoolId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._stream_pool_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def stream_pool_id(self):
        """
        Gets the stream_pool_id of this UpdateStreamDetails.
        The `OCID`__ of the stream pool where the stream should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The stream_pool_id of this UpdateStreamDetails.
        :rtype: str
        """
        return self._stream_pool_id

    @stream_pool_id.setter
    def stream_pool_id(self, stream_pool_id):
        """
        Sets the stream_pool_id of this UpdateStreamDetails.
        The `OCID`__ of the stream pool where the stream should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param stream_pool_id: The stream_pool_id of this UpdateStreamDetails.
        :type: str
        """
        self._stream_pool_id = stream_pool_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateStreamDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateStreamDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateStreamDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateStreamDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateStreamDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateStreamDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateStreamDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateStreamDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
