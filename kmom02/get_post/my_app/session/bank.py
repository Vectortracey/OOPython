import json
from account import Account, Checkingaccount

class Bank():
    def __init__(self):
        self.accounts = []
        self._create_default_accounts()

    def _create_default_accounts(self):
        accounts_json = json.load(open("static/data/accounts.json", encoding="utf-8"))

        for acc in accounts_json:
            self.accounts.append(Account.create_from_json(acc))

    def add_account(self, data):
        if data["type"] == Account.__name__:
            self.accounts.append(Account.create_from_json(data))
        elif data["type"] == Checkingaccount.__name__:
            self.accounts.append(Checkingaccount.create_from_json(data))

    def save_data(self):
        json_data = []
        for acc in self.accounts:
            json_data.append(acc.serialize())
        json.dump(json_data, open("static/data/accounts.json", "w",encoding="utf-8"), indent=4)




