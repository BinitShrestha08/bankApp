class Account:
    def __init__(self, accountType):
        self. accountType = accountType
        self.balance = 0.0

    def read_balance(self):
        self.balance = float(
            input("Enter the current balance for {} account: $".format(self.accountType)))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("${:.2f} deposited into {} account.".format(
                amount, self.accountType))
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("${:.2f} withdrawn from {} account.".format(
                amount, self.accountType))
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def showBalance(self):
        print("{} account balance: ${:.2f}".format(
            self.accountType, self.balance))

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print("${:.2f} transferred from {} to {} account.".format(
                amount, self.accountType, target_account.accountType))
        else:
            print("Insufficient funds or invalid transfer amount.")

    def __str__(self):
        return "{} balance $:{:.2f}".format(self.accountType, self.balance)
