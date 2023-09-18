from manager import Manager
from customer import Customer


class Bank:
    def __init__(self):
        self.manager = Manager('ok')
        self.customers = []

    # descriptive function on python like as ones in java
    # def __str__(self) -> str:
    #     return print(f'{manager_instance}')

    def customerLogin():
        pass

    def view():
        pass

    def use(self):
        print('-------------------------')
        print('L- Login to customer menu')
        print('V- View all customer')
        print('x-exit')
        print('-------------------------')

        choice = input('Banking menu (L/V/X): ')

        while choice != 'X':

            match choice:
                case 'L':
                    self.customerLogin()

                case 'V':
                    self.view()

                case _:
                    print('Unknown case!')

            choice = input('Start banking (d/w/s/x): ')


def main():
    bank = Bank()
    bank.use()


if __name__ == "__main__":
    main()
