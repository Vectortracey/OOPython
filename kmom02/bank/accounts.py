"""
module that contains account and savingsaccount
"""

class Account():
    """
    an account class
    """
    account_number = 1
    transaction_fee = 0.01

    def __init__(self, balance):
        self._id = Account.account_number
        self._balance = balance
        Account.account_number += 1

    @property
    def type_(self):
        """
        returns the type
        """
        return self.__class__.__name__

    @classmethod
    def create_account(cls, data):
        """
        returns balance
        """
        return cls(data["balance"])

    @property
    def balance(self):
        """
        returns balance
        """
        return self._balance

    @property
    def id_(self):
        """
        returns the id
        """
        return self._id

    def serialize(self):
        """
        serialize the information
        """
        return {
            "type": self.__class__.__name__,
            "balance": self.balance
        }

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @classmethod
    def calculate_transaction_fee(cls, amount):
        """
        calculates transactions fee and returns the amount
        """
        return cls.transaction_fee * amount




class SavingsAccount(Account):
    """
    savingsaccount function inherits from Account function
    """
    interest_rate = 0.0015
    transaction_fee = 0.013

    def calculate_daily_interest_rate(self):
        """
        calculate the daiuly interest rates
        """
        return self.interest_rate * self.balance / 365
