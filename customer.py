from account import Account


class Customer:
    def __init__(self, name):
        self.name = name
        self.savings = Account("Savings")
        self.loan = Account("Loan")

    def read_amount(self):
        return float(input("Enter the amount: $"))

    def withdraw(self):
        amount = self.read_amount()
        self.savings.withdraw(amount)

    def deposit(self):
        amount = self.read_amount()
        self.savings.deposit(amount)

    def transfer(self):
        amount = self.read_amount()
        self.savings.transfer(amount, self.loan)

    def show(self):
        print(self)

    def __str__(self):
        output = self.name + 'savings account has'
        output += str(self.savings) + '\n'
        output += str(self.loan) + '\n'
        return output

    def showBalance(self):
        self.customer.show()

    def deposit(self):
        self.customer.deposit()

    def withdraw(self):
        self.customer.withdraw()

    def transfer(self):
        self.customer.transfer()

    def use(self):
        print('-------------------------')
        print('d-make deposit')
        print('w-withdraw')
        print('s-show balance')
        print('t-transfer')
        print('x-exit')
        print('-------------------------')

        choice = input(f'{ self.name} Banking Menu (d/w/s/t/x): ')

        while choice != 'x':

            match choice:
                case 's':
                    self.showBalance()

                case 'd':
                    self.deposit()

                case 'w':
                    self.withdraw()
                case _:
                    print('Unknown case!')

            choice = input(f'{ self.name} Start banking (d/w/s/x): ')
