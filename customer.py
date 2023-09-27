from account import Account


class Customer:
    def __init__(self, name):
        self.name = name if name else self.read_name()
        self.savings = Account("Savings")
        self.loan = Account("Loan")

    def read_name(self):
        return input("Name: ")

    def read_balance(self, account_type):
        return float(input(f"Enter {account_type} balance for {self.name}: $"))

    def read_amount(self):
        return float(input("Enter the amount: $"))

    def withdraw(self):
        try:
            amount = self.read_amount()
            if self.savings.has(amount):
                self.savings.withdraw(amount)
                print(
                    f"${amount:.2f} withdrawn from {self.name}'s savings account.")
            else:
                print("Insufficient funds in savings account.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def deposit(self):
        amount = float(
            input(f"Amount to deposit into {self.name}'s savings account: $"))
        if amount > 0:
            self.savings.deposit(amount)
            print(f"${amount:.2f} deposited into {self.name}'s savings account.")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def transfer(self):
        try:
            amount = self.read_amount()
            if self.savings.has(amount):
                self.savings.transfer(amount, self.loan)
                print(
                    f"${amount:.2f} transferred from {self.name}'s savings account to loan account.")
            else:
                print("Insufficient funds in savings account.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def show(self):
        print(self)

    def __str__(self):
        return f"{self.name} --> {self.savings} | {self.loan}"

    def show_balance(self):
        self.show()

    def use(self):
        print('-------------------------')
        print('d-make deposit')
        print('w-withdraw')
        print('s-show balance')
        print('t-transfer')
        print('x-exit')
        print('-------------------------')

        choice = input(f'{self.name} Banking Menu (d/w/s/t/x): ')

        while choice != 'x':

            match choice:
                case 's':
                    self.show_balance()

                case 'd':
                    self.deposit()

                case 'w':
                    self.withdraw()

                case 't':
                    self.transfer()

                case _:
                    print('Unknown case!')

            choice = input(f'{self.name} Start banking (d/w/s/t/x): ')
