from abc import ABC, abstractmethod

class Bank:

    def __init__(self):
        self.customers = []
        self.admins = []

    def create_customer_account(self):
        self.new_customer = Customer()
        self.customers.append(self.new_customer)

    def delete_customer_account(self):
        for i in range(len(self.customers)):
            print(i, self.customers[i])
        self.customers.remove(int(input("Which customer to delete? ")))

class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, date):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
        self.detail_list = [self.transaction_id, self.transaction_type, self.amount, self.date]

    def get_transaction_details(self, transaction_id):
        if transaction_id in self.detail_list:
            return self.detail_list
        else:
            print("Invalid Transaction ID")


class Person(ABC):

    @abstractmethod
    def get_details(self):
        pass

class Admin(Person):

    def __init__(self):
        self.name = input("Name: ")
        self.address = input("Address: ")
        self.phoneno = input("Contact no: ")

    def get_details(self):
        print("Name: ", self.name, "\n", "Address: ", self.address,"\n", "Contact no: ", self.phoneno)

class Customer(Person):

    def __init__(self):
        self.name = input("Name: ")
        self.address = input("Address: ")
        self.phoneno = input("Contact no: ")

    def add_account(self):
        self.account = Account()
        self.accounts_list.append(self.account)

    

    def get_details(self):
        print("Name: ", self.name, "\n", "Address: ", self.address,"\n", "Contact no: ", self.phoneno)

class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def show_account_details(self):
        pass


        


class SavingsAccount(Account):

    def __init__(self):
        self.account_no = input("Account no: ")
        self.balance = input("Balance: ")
        self.owner = Customer()
        self.interest_rate = input("Interest rate offered:")

    def apply_interest(self, time_period):
        return self.balance + (self.balance*self.interest_rate)*time_period
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount

    def get_balance(self):
        print(self.balance)

    def show_account_details(self):
        print("Account no:", self.account_no)
        print("Balance:", self.balance)
        print("Owner: ", self.owner)


class BusinessAccount(Account):

    def __init__(self):
        self.account_no = input("Account no: ")
        self.balance = input("Balance: ")
        self.owner = Customer()
        self.overdraft_limit = input("Overdraft limit offered:")
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount

    def get_balance(self):
        print(self.balance)

    def show_account_details(self):
        print("Account no:", self.account_no)
        print("Balance:", self.balance)
        print("Owner: ", self.owner)

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit

    def override_withdraw(self, amount):
        pass


class Menu():

    
    def __init__(self):

        self.exit = False

        while(not self.exit):
            
            print("""

                  Bank Management 1.0
                  1. Admin Login
                  2. Deposit
                  3. Withdraw
                  4. Check Balance
                  5. Transaction History
                  7. Calculate Interest
                  8. Exit

                """)
            
            option = int(input("Enter your choice: "))
            
            if option == 1:
                print("""

                Admin Dashboard:
                      1. Create Account
                      2. Set/Change Overdraft Limit
                      3. Delete Account
                      4. Exit
                    
                      """)
                choice = int(input(": "))

                if choice == 1:
                    type = int(input("1. Create Savings Account \n 2. Create Business Account \n: "))

                    if type == 1:
                        self.ac = SavingsAccount()

                    elif type == 2:
                        self.ac = BusinessAccount()

                    else:
                        print("Invalid Choice")
                
                elif choice == 2:
                    pass
                
                elif choice == 3:
                    pass
                
                elif choice == 4:
                    pass

                else:
                    print("Invalid choice!")
                    

            elif option == 2:
                pass
            
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                pass
            elif option == 7:
                pass
            elif option == 8:
                pass
            elif option == 9:
                pass
            elif option == 10:
                pass
            elif option == 11:
                break
            
            else:
                print("Invalid Choice")


Start = Menu()