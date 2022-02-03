#!/usr/bin/env python3
"""
module that contains the accountmanager function for bank
"""
import json
from datetime import date
from accounts import Account, SavingsAccount


class AccountManager():
    """
    account manager function
    """
    _CLASSES = {
        "Account": Account,
        "SavingsAccount": SavingsAccount
    }

    def __init__(self):
        self._accounts = []
        self.load_data()

    def get_account_by_id(self, id_):
        """
        get the account with the id_
        """
        for acc in self.accounts:
            if acc.id_ == id_:
                matching_acc = acc
        return matching_acc

    def save_data(self):
        """
        save account to json file
        """
        json_data = [acc.serialize() for acc in self.accounts]
        json.dump(json_data, open("static/data/data.json", "w", encoding="utf-8"), indent=4)

    def load_data(self):
        """
        load account from json
        """
        accounts_json = json.load(open("static/data/data.json", encoding="utf-8"))

        for acc in accounts_json:
            self.add_account(acc)

    def add_account(self, acc):
        """
        add a new account
        """
        self.accounts.append(self._CLASSES[acc["type"]].create_account(acc))

    def transfer(self, data):
        """
        function that transfers money betweens accounts
        """
        from_account = self.get_account_by_id(int(data["from_account"]))
        to_account = self.get_account_by_id(int(data["to_account"]))
        amount = float(data["amount"])
        transaction_fee = from_account.calculate_transaction_fee(amount)
        from_account.balance -= amount
        to_account.balance += amount - transaction_fee

    @property
    def accounts(self):
        """
        property accounts function that returns accounts
        """
        return self._accounts

    @staticmethod
    def calculate_interest_rate(account, date_):
        """
        static method that returns the interest
        """
        daily_interest = account.calculate_daily_interest_rate()
        num_days = date.fromisoformat(date_) - date.today()
        num_days = num_days.days
        interest_rate = daily_interest * num_days
        return interest_rate
