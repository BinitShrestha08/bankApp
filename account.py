class Account:
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = self.read_balance()

    def read_balance(self):
        return float(input(f"Initial {self.account_type} balance $"))

    def has(self, amount):
        return self.balance >= amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def pay_to(self, amount, target_account):
        self.balance -= amount
        target_account.balance += amount

    def __str__(self):
        return f"{self.account_type} account has ${self.balance:.2f}"

    def transfer(self, amount, target_account):
        self.balance -= amount
        target_account.balance += amount
