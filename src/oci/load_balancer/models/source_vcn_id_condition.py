# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .rule_condition import RuleCondition
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceVcnIdCondition(RuleCondition):
    """
    An access control rule condition that requires a match on the specified source VCN OCID.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SourceVcnIdCondition object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.SourceVcnIdCondition.attribute_name` attribute
        of this class is ``SOURCE_VCN_ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this SourceVcnIdCondition.
            Allowed values for this property are: "SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH"
        :type attribute_name: str

        :param attribute_value:
            The value to assign to the attribute_value property of this SourceVcnIdCondition.
        :type attribute_value: str

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_value': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_value': 'attributeValue'
        }

        self._attribute_name = None
        self._attribute_value = None
        self._attribute_name = 'SOURCE_VCN_ID'

    @property
    def attribute_value(self):
        """
        **[Required]** Gets the attribute_value of this SourceVcnIdCondition.
        The `OCID`__ of the originating VCN that an incoming packet
        must match.

        You can use this condition in conjunction with `SourceVcnIpAddressCondition`.

        **NOTE:** If you define this condition for a rule without a `SourceVcnIpAddressCondition`, this condition
        matches all incoming traffic in the specified VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The attribute_value of this SourceVcnIdCondition.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """
        Sets the attribute_value of this SourceVcnIdCondition.
        The `OCID`__ of the originating VCN that an incoming packet
        must match.

        You can use this condition in conjunction with `SourceVcnIpAddressCondition`.

        **NOTE:** If you define this condition for a rule without a `SourceVcnIpAddressCondition`, this condition
        matches all incoming traffic in the specified VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param attribute_value: The attribute_value of this SourceVcnIdCondition.
        :type: str
        """
        self._attribute_value = attribute_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
