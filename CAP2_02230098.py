# Importing necessary modules:
import os # os: Provides a way of using operating system dependent functionality.
import json # json: Implements JSON (JavaScript Object Notation), a lightweight data-interchange format.
import random # random: Contains functions for generating random numbers.
import string # string: Contains various string constants and classes, plus low-level operations on strings.

# Initialize the list to hold bank account objects
accounts = []

# Define the BankAccount class with methods for deposit, withdrawal, and transfer operations
class BankAccount:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    # Deposit method to increase the account balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        self.update_account_balance()

    # Withdrawal method to decrease the account balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            self.update_account_balance()
        else:
            print("Insufficient balance.")

    # Transfer method to move funds between accounts
    def transfer(self, recipient_account, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            self.update_account_balance()
            recipient_account.update_account_balance()  # Ensure recipient's balance is updated
            print(f"Transferred {amount} to account {recipient_account.account_number}.")
        else:
            print("Insufficient balance.")

    # Method to update the account balance in the accounts list and file
    def update_account_balance(self):
        for account_dict in accounts:
            if account_dict["account_number"] == self.account_number:
                account_dict["balance"] = self.balance
                break

        with open("accounts.txt", "w") as file:
            json.dump(accounts, file, default=lambda obj: obj.__dict__)

# Define the Account class, inheriting from BankAccount, to handle personal and business accounts
class Account(BankAccount):
    def __init__(self, account_number, account_type, password, balance=0):
        super().__init__(account_number, account_type, balance)
        self.password = password

# Function to create a new account, including generating a unique account number and password
def create_account():
    account_type = input("Enter account type (Personal(p)/Business(b)): ").lower()
    if account_type == "personal" or account_type == "p":
        account_type_str = "Personal"
    elif account_type == "business" or account_type == "b":
        account_type_str = "Business"
    else:
        print("Invalid account type.")
        return

    account_number = generate_account_number()
    password = generate_password()
    account = Account(account_number, account_type_str, password)
    print(f"{account_type_str} account created. Account number: {account_number}, Password: {password}")
    save_account(account)

# Function to generate a unique account number based on the current length of the accounts list
def generate_account_number():
    return str(len(accounts) + 1).zfill(3)

# Function to generate a secure password using ASCII letters and digits
def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=5))

# Function to save an account object to the accounts list and file
def save_account(account):
    accounts.append(account.__dict__)
    with open("accounts.txt", "w") as file:
        json.dump(accounts, file, default=lambda obj: obj.__dict__)

# Function to log in to an account by matching the entered account number and password
def login():
    account_number = input("Enter your account number: ")
    for account_dict in accounts:
        if account_dict["account_number"] == account_number:
            password = input("Enter your password: ")
            if account_dict["password"] == password:
                return Account(**account_dict)
            else:
                print("Invalid password.")
    print("Invalid account number.")

# Function to delete an account from the accounts list and file
def delete_account(account):
    accounts.remove(account.__dict__)
    with open("accounts.txt", "w") as file:
        json.dump(accounts, file, default=lambda obj: obj.__dict__)
    print("Account deleted successfully.")

# Load existing accounts from the file if it exists
if os.path.exists("accounts.txt"):
    with open("accounts.txt", "r") as file:
        accounts = json.load(file)

# Main program loop to interact with the user
while True:
    print("Welcome to My Bank. Are you a new customer? If yes then, please create an account or sign up or if you are an existing customer, please Sign in.")
    print("0. Create Account/Sign Up")
    print("1. Sign In")
    print("2. Logout/Exit")
    choice = input("Enter your option: ")

    if choice == "0":
        create_account()
    elif choice == "1":
        account = login()
        if account:
            print(f"Welcome to your {account.account_type} account!")
            while True:
                print("Check Balance - (press 1)")
                print("Deposit - (press 2)")
                print("Withdraw - (press 3)")
                print("Transfer - (press 4)")
                print("Delete Account - (press 5)")
                print("Sign out - (press 6)")
                option = input("Enter your option: ")

                if option == "1":
                    print(f"Your Balance is: {account.balance}")
                elif option == "2":
                    amount = float(input("Enter your amount to deposit: "))
                    account.deposit(amount)
                elif option == "3":
                    amount = float(input("Enter your amount to withdraw: "))
                    account.withdraw(amount)
                elif option == "4":
                    recipient_number = input("Enter the recipient account number: ")
                    recipient = next((acc for acc in accounts if acc["account_number"] == recipient_number), None)
                    if recipient:
                        recipient = Account(**recipient)
                        amount = float(input("Enter amount to transfer: "))
                        account.transfer(recipient, amount)
                    else:
                        print("Invalid recipient account number.")
                elif option == "5":
                    delete_account(account)
                    break
                elif option == "6":
                    break
                else:
                    print("Invalid option.")
    elif choice == "2":
        break
    else:
        print("Invalid choice.")
