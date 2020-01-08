# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferApplianceEncryptionPassphrase(object):
    """
    TransferApplianceEncryptionPassphrase model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TransferApplianceEncryptionPassphrase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_passphrase:
            The value to assign to the encryption_passphrase property of this TransferApplianceEncryptionPassphrase.
        :type encryption_passphrase: str

        """
        self.swagger_types = {
            'encryption_passphrase': 'str'
        }

        self.attribute_map = {
            'encryption_passphrase': 'encryptionPassphrase'
        }

        self._encryption_passphrase = None

    @property
    def encryption_passphrase(self):
        """
        Gets the encryption_passphrase of this TransferApplianceEncryptionPassphrase.

        :return: The encryption_passphrase of this TransferApplianceEncryptionPassphrase.
        :rtype: str
        """
        return self._encryption_passphrase

    @encryption_passphrase.setter
    def encryption_passphrase(self, encryption_passphrase):
        """
        Sets the encryption_passphrase of this TransferApplianceEncryptionPassphrase.

        :param encryption_passphrase: The encryption_passphrase of this TransferApplianceEncryptionPassphrase.
        :type: str
        """
        self._encryption_passphrase = encryption_passphrase

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
