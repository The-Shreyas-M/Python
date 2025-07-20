from abc import ABC, abstractmethod
from datetime import datetime

# Base Classes
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_details(self):
        return {
            "Name": self.name,
            "Address": self.address,
            "Phone": self.phone
        }

class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self._balance = balance
        self.owner = owner

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def show_account_details(self):
        return {
            "Account Number": self.account_number,
            "Balance": self._balance,
            "Owner": self.owner.get_details()
        }

# Derived Classes
class Customer(Person):
    def __init__(self, name, address, phone):
        super().__init__(name, address, phone)
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        self.accounts = [acc for acc in self.accounts if acc.account_number != account_number]

    def get_accounts_summary(self):
        return [account.show_account_details() for account in self.accounts]

class Admin(Person):
    def __init__(self, name, address, phone, employee_id):
        super().__init__(name, address, phone)
        self.employee_id = employee_id

    def approve_account(self, customer, account):
        customer.add_account(account)

class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

class BusinessAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=1000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self._balance -= amount

class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, account):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now()
        self.account = account

    def get_transaction_details(self):
        return {
            "Transaction ID": self.transaction_id,
            "Type": self.transaction_type,
            "Amount": self.amount,
            "Date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "Account Number": self.account.account_number
        }

class Bank:
    def __init__(self):
        self.customers = []
        self.admins = []
        self.transactions = []

    def create_customer_account(self, name, address, phone, account_type, **kwargs):
        customer = Customer(name, address, phone)
        account_number = f"ACCT{len(self.customers) + 1}"
        if account_type == "Savings":
            account = SavingsAccount(account_number, customer, kwargs.get("balance", 0), kwargs.get("interest_rate", 0.02))
        elif account_type == "Business":
            account = BusinessAccount(account_number, customer, kwargs.get("balance", 0), kwargs.get("overdraft_limit", 1000))
        else:
            raise ValueError("Invalid account type.")
        customer.add_account(account)
        self.customers.append(customer)
        return customer, account

    def delete_customer_account(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    customer.remove_account(account_number)
                    return "Account deleted."
        raise ValueError("Account not found.")

    def view_transaction_history(self, account_number):
        return [txn.get_transaction_details() for txn in self.transactions if txn.account.account_number == account_number]

    def find_customer_by_account(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    return customer
        raise ValueError("Account not found.")

# Menu-driven program
if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\n=== Banking System Menu ===")
        print("1. Create Customer Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            phone = input("Enter customer phone: ")
            account_type = input("Enter account type (Savings/Business): ")
            initial_balance = float(input("Enter initial balance: "))

            if account_type == "Savings":
                interest_rate = float(input("Enter interest rate: "))
                customer, account = bank.create_customer_account(name, address, phone, account_type, balance=initial_balance, interest_rate=interest_rate)
            elif account_type == "Business":
                overdraft_limit = float(input("Enter overdraft limit: "))
                customer, account = bank.create_customer_account(name, address, phone, account_type, balance=initial_balance, overdraft_limit=overdraft_limit)
            else:
                print("Invalid account type.")
                continue

            print(f"Account created successfully! Account Number: {account.account_number}")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))

            customer = bank.find_customer_by_account(account_number)
            for account in customer.accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    transaction = Transaction(f"TXN{len(bank.transactions) + 1}", "Deposit", amount, account)
                    bank.transactions.append(transaction)
                    print("Deposit successful.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))

            customer = bank.find_customer_by_account(account_number)
            for account in customer.accounts:
                if account.account_number == account_number:
                    try:
                        account.withdraw(amount)
                        transaction = Transaction(f"TXN{len(bank.transactions) + 1}", "Withdrawal", amount, account)
                        bank.transactions.append(transaction)
                        print("Withdrawal successful.")
                    except ValueError as e:
                        print(e)

        elif choice == "4":
            account_number = input("Enter account number: ")
            customer = bank.find_customer_by_account(account_number)
            for account in customer.accounts:
                if account.account_number == account_number:
                    print(account.show_account_details())

        elif choice == "5":
            account_number = input("Enter account number: ")
            transactions = bank.view_transaction_history(account_number)
            if transactions:
                for txn in transactions:
                    print(txn)
            else:
                print("No transactions found.")

        elif choice == "6":
            print("Exiting... Thank you for using the Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")
