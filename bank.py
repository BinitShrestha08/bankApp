from manager import Manager
from customer import Customer
from datetime import datetime


class Bank:
    DTF = "%d/%m/%Y - %H:%M:%S"
    NOW = datetime.now()

    def __init__(self):
        self.manager = Manager()
        self.customers = []

    # descriptive function on python like as ones in java
    # def __str__(self) -> str:
    #     return print(f'{manager_instance}')

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def customer_login(self):
        # Find the customer by name
        customer_name = input("Enter customer name: ")
        found = self.find_customer(customer_name)
        if found != None:
            found.use()
        else:
            print('Customer not found')

    def view(self):
        for customer in self.customers:
            print(customer)

    def addCustomer(self):
        customer_name = input("Enter customer name: ")
        found = self.find_customer(customer_name)
        if found is None:
            self.customers.append(Customer(customer_name))
            print(f'Customer {customer_name} added successfully.')

        else:
            print('Customer already exists.')

    def deleteCustomer(self):
        customer_name = input("Enter customer name: ")
        found = self.find_customer(customer_name)
        if found is None:
            print('Customer does not exists.')
        else:
            self.customers.remove(found)
            print(f'Customer {found} deleted successfully.')

    def show(self):
        customer_name = input("Enter customer name: ")

        found = self.find_customer(customer_name)
        if found is None:
            print(f'Customer {customer_name} does not exist.')
        else:
            print(found)

    def admin_login(self):
        self.manager.login(self)

    def menu(self):
        print(f"Banking menu: {Bank.NOW.strftime(Bank.DTF)}")
        print('-------------------------')
        print('L- Login to customer menu')
        print('A- Login to Admin menu')
        # print('V- View all customer')
        print('x-exit')
        print('-------------------------')

        choice = input('Banking menu (L/A/X): ')

        while choice != 'X':

            match choice:
                case 'L':
                    self.customer_login()
                case 'A':
                    self.admin_login()

                case _:
                    print('Unknown case!')

            choice = input('Banking menu (L/A/X): ')


def main():
    bank = Bank()
    # manager = Manager(bank)
    for i in range(2):
        customer_name = input(f"Enter customer {i+1} name: ")
        customer = Customer(customer_name)
        bank.customers.append(customer)

    bank.menu()


if __name__ == "__main__":
    main()
