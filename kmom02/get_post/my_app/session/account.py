import json
class Account():
    """
    A account class
    """
    interest = 1.05
    def __init__(self, name, balance, owner):
        self._balance = balance
        self.name = name
        self.owner = owner

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        raise ValueError("Not enough on your acoount")

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @classmethod
    def calculate(cls, amount):
        return amount * cls.interest

    @classmethod
    def create_from_json(cls, data):
        """
        Retrives data from json file
        """
        return cls(data["name"], data["balance"], data["owner"])

    def serialize(self):
        return  {
            "balance": self._balance,
            "name": self.name,
            "owner": self.owner,
            "type": self.__class__.__name__
        }


    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

class Checkingaccount(Account):
    TRANSACTION_FEE = 50
    TRANSACTION_LIMIT = 3

    def __init__(self, name, balance, owner, trans_counter=0):
        super().__init__(name, balance, owner)
        self.transaciton_counter = trans_counter

    def withdraw(self, amount):
        super().withdraw(amount)
        self.transaciton_counter += 1
        if self.transaciton_counter > self.TRANSACTION_LIMIT:
            self._balance -= self.TRANSACTION_FEE
        return self._balance


    def serialize(self):
       ser_dict = super().serialize()
       ser_dict["trans_counter"] = self.transaciton_counter
       return ser_dict

    @classmethod
    def create_from_json(cls, data):
        return cls(data["name"], data["balance"], data["owner"], data.get("trans_counter", 0))