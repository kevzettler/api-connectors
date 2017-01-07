# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [Changelog](/app/apiChangelog)  ----  #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ---  ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Wallet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account=None, currency=None, prev_deposited=None, prev_withdrawn=None, prev_amount=None, prev_timestamp=None, delta_deposited=None, delta_withdrawn=None, delta_amount=None, deposited=None, withdrawn=None, amount=None, pending_credit=None, pending_debit=None, confirmed_debit=None, timestamp=None, addr=None):
        """
        Wallet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account': 'float',
            'currency': 'str',
            'prev_deposited': 'float',
            'prev_withdrawn': 'float',
            'prev_amount': 'float',
            'prev_timestamp': 'date',
            'delta_deposited': 'float',
            'delta_withdrawn': 'float',
            'delta_amount': 'float',
            'deposited': 'float',
            'withdrawn': 'float',
            'amount': 'float',
            'pending_credit': 'float',
            'pending_debit': 'float',
            'confirmed_debit': 'float',
            'timestamp': 'date',
            'addr': 'str'
        }

        self.attribute_map = {
            'account': 'account',
            'currency': 'currency',
            'prev_deposited': 'prevDeposited',
            'prev_withdrawn': 'prevWithdrawn',
            'prev_amount': 'prevAmount',
            'prev_timestamp': 'prevTimestamp',
            'delta_deposited': 'deltaDeposited',
            'delta_withdrawn': 'deltaWithdrawn',
            'delta_amount': 'deltaAmount',
            'deposited': 'deposited',
            'withdrawn': 'withdrawn',
            'amount': 'amount',
            'pending_credit': 'pendingCredit',
            'pending_debit': 'pendingDebit',
            'confirmed_debit': 'confirmedDebit',
            'timestamp': 'timestamp',
            'addr': 'addr'
        }

        self._account = account
        self._currency = currency
        self._prev_deposited = prev_deposited
        self._prev_withdrawn = prev_withdrawn
        self._prev_amount = prev_amount
        self._prev_timestamp = prev_timestamp
        self._delta_deposited = delta_deposited
        self._delta_withdrawn = delta_withdrawn
        self._delta_amount = delta_amount
        self._deposited = deposited
        self._withdrawn = withdrawn
        self._amount = amount
        self._pending_credit = pending_credit
        self._pending_debit = pending_debit
        self._confirmed_debit = confirmed_debit
        self._timestamp = timestamp
        self._addr = addr

    @property
    def account(self):
        """
        Gets the account of this Wallet.


        :return: The account of this Wallet.
        :rtype: float
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Wallet.


        :param account: The account of this Wallet.
        :type: float
        """

        self._account = account

    @property
    def currency(self):
        """
        Gets the currency of this Wallet.


        :return: The currency of this Wallet.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Wallet.


        :param currency: The currency of this Wallet.
        :type: str
        """

        self._currency = currency

    @property
    def prev_deposited(self):
        """
        Gets the prev_deposited of this Wallet.


        :return: The prev_deposited of this Wallet.
        :rtype: float
        """
        return self._prev_deposited

    @prev_deposited.setter
    def prev_deposited(self, prev_deposited):
        """
        Sets the prev_deposited of this Wallet.


        :param prev_deposited: The prev_deposited of this Wallet.
        :type: float
        """

        self._prev_deposited = prev_deposited

    @property
    def prev_withdrawn(self):
        """
        Gets the prev_withdrawn of this Wallet.


        :return: The prev_withdrawn of this Wallet.
        :rtype: float
        """
        return self._prev_withdrawn

    @prev_withdrawn.setter
    def prev_withdrawn(self, prev_withdrawn):
        """
        Sets the prev_withdrawn of this Wallet.


        :param prev_withdrawn: The prev_withdrawn of this Wallet.
        :type: float
        """

        self._prev_withdrawn = prev_withdrawn

    @property
    def prev_amount(self):
        """
        Gets the prev_amount of this Wallet.


        :return: The prev_amount of this Wallet.
        :rtype: float
        """
        return self._prev_amount

    @prev_amount.setter
    def prev_amount(self, prev_amount):
        """
        Sets the prev_amount of this Wallet.


        :param prev_amount: The prev_amount of this Wallet.
        :type: float
        """

        self._prev_amount = prev_amount

    @property
    def prev_timestamp(self):
        """
        Gets the prev_timestamp of this Wallet.


        :return: The prev_timestamp of this Wallet.
        :rtype: date
        """
        return self._prev_timestamp

    @prev_timestamp.setter
    def prev_timestamp(self, prev_timestamp):
        """
        Sets the prev_timestamp of this Wallet.


        :param prev_timestamp: The prev_timestamp of this Wallet.
        :type: date
        """

        self._prev_timestamp = prev_timestamp

    @property
    def delta_deposited(self):
        """
        Gets the delta_deposited of this Wallet.


        :return: The delta_deposited of this Wallet.
        :rtype: float
        """
        return self._delta_deposited

    @delta_deposited.setter
    def delta_deposited(self, delta_deposited):
        """
        Sets the delta_deposited of this Wallet.


        :param delta_deposited: The delta_deposited of this Wallet.
        :type: float
        """

        self._delta_deposited = delta_deposited

    @property
    def delta_withdrawn(self):
        """
        Gets the delta_withdrawn of this Wallet.


        :return: The delta_withdrawn of this Wallet.
        :rtype: float
        """
        return self._delta_withdrawn

    @delta_withdrawn.setter
    def delta_withdrawn(self, delta_withdrawn):
        """
        Sets the delta_withdrawn of this Wallet.


        :param delta_withdrawn: The delta_withdrawn of this Wallet.
        :type: float
        """

        self._delta_withdrawn = delta_withdrawn

    @property
    def delta_amount(self):
        """
        Gets the delta_amount of this Wallet.


        :return: The delta_amount of this Wallet.
        :rtype: float
        """
        return self._delta_amount

    @delta_amount.setter
    def delta_amount(self, delta_amount):
        """
        Sets the delta_amount of this Wallet.


        :param delta_amount: The delta_amount of this Wallet.
        :type: float
        """

        self._delta_amount = delta_amount

    @property
    def deposited(self):
        """
        Gets the deposited of this Wallet.


        :return: The deposited of this Wallet.
        :rtype: float
        """
        return self._deposited

    @deposited.setter
    def deposited(self, deposited):
        """
        Sets the deposited of this Wallet.


        :param deposited: The deposited of this Wallet.
        :type: float
        """

        self._deposited = deposited

    @property
    def withdrawn(self):
        """
        Gets the withdrawn of this Wallet.


        :return: The withdrawn of this Wallet.
        :rtype: float
        """
        return self._withdrawn

    @withdrawn.setter
    def withdrawn(self, withdrawn):
        """
        Sets the withdrawn of this Wallet.


        :param withdrawn: The withdrawn of this Wallet.
        :type: float
        """

        self._withdrawn = withdrawn

    @property
    def amount(self):
        """
        Gets the amount of this Wallet.


        :return: The amount of this Wallet.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Wallet.


        :param amount: The amount of this Wallet.
        :type: float
        """

        self._amount = amount

    @property
    def pending_credit(self):
        """
        Gets the pending_credit of this Wallet.


        :return: The pending_credit of this Wallet.
        :rtype: float
        """
        return self._pending_credit

    @pending_credit.setter
    def pending_credit(self, pending_credit):
        """
        Sets the pending_credit of this Wallet.


        :param pending_credit: The pending_credit of this Wallet.
        :type: float
        """

        self._pending_credit = pending_credit

    @property
    def pending_debit(self):
        """
        Gets the pending_debit of this Wallet.


        :return: The pending_debit of this Wallet.
        :rtype: float
        """
        return self._pending_debit

    @pending_debit.setter
    def pending_debit(self, pending_debit):
        """
        Sets the pending_debit of this Wallet.


        :param pending_debit: The pending_debit of this Wallet.
        :type: float
        """

        self._pending_debit = pending_debit

    @property
    def confirmed_debit(self):
        """
        Gets the confirmed_debit of this Wallet.


        :return: The confirmed_debit of this Wallet.
        :rtype: float
        """
        return self._confirmed_debit

    @confirmed_debit.setter
    def confirmed_debit(self, confirmed_debit):
        """
        Sets the confirmed_debit of this Wallet.


        :param confirmed_debit: The confirmed_debit of this Wallet.
        :type: float
        """

        self._confirmed_debit = confirmed_debit

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Wallet.


        :return: The timestamp of this Wallet.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Wallet.


        :param timestamp: The timestamp of this Wallet.
        :type: date
        """

        self._timestamp = timestamp

    @property
    def addr(self):
        """
        Gets the addr of this Wallet.


        :return: The addr of this Wallet.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """
        Sets the addr of this Wallet.


        :param addr: The addr of this Wallet.
        :type: str
        """

        self._addr = addr

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other