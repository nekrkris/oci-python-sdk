# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShippingVendors(object):
    """
    ShippingVendors model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShippingVendors object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vendors:
            The value to assign to the vendors property of this ShippingVendors.
        :type vendors: list[str]

        """
        self.swagger_types = {
            'vendors': 'list[str]'
        }

        self.attribute_map = {
            'vendors': 'vendors'
        }

        self._vendors = None

    @property
    def vendors(self):
        """
        Gets the vendors of this ShippingVendors.
        List of available shipping vendors for package delivery


        :return: The vendors of this ShippingVendors.
        :rtype: list[str]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """
        Sets the vendors of this ShippingVendors.
        List of available shipping vendors for package delivery


        :param vendors: The vendors of this ShippingVendors.
        :type: list[str]
        """
        self._vendors = vendors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
