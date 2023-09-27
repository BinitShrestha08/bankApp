class Manager:
    def __init__(self):
        self.name = "John Smith"

    def view(self, bank):
        
        bank.view()

    def add(self, bank):
        bank.addCustomer()

    def remove(self, bank):
        bank.deleteCustomer()

    def show(self, bank):
        bank.show()

    def read_choice(self):
        print(self.name + " choices(a/r/s/v/x): ")
        return input().strip().lower()

    def login(self, bank):
        print(self.name + " admin menu " + bank.NOW.strftime(bank.DTF))
        choice = self.read_choice()
        while choice != 'x':
            if choice == 'a':
                self.add(bank)
            elif choice == 'r':
                self.remove(bank)
            elif choice == 's':
                self.show(bank)
            elif choice == 'v':
                self.view(bank)
            else:
                self.help()

            choice = self.read_choice()

    @staticmethod
    def help():
        print("a - add")
        print("r - remove")
        print("s - show")
        print("v - view")
        print("x - exit")
