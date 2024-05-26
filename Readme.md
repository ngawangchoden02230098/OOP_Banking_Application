#  OOP Banking Application

This is a simple command-line banking application built using Python. It allows users to create personal or business bank accounts, deposit and withdraw funds, transfer money between accounts, and delete their accounts.

## Features

- Create new personal or business bank accounts
- Log in to an existing account
- Check account balance
- Deposit money into an account
- Withdraw money from an account
- Transfer funds between accounts
- Delete an account

## Getting Started

1. Clone the repository or download the code files.
2. Make sure you have Python installed on your system.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the `banking_app.py` file using the following command:

5. Follow the on-screen instructions to interact with the banking application.

## How It Works

1. Upon running the application, you will be presented with a menu to create a new account, sign in to an existing account, or exit the program.

2. If you choose to create a new account, you will be prompted to enter the account type (personal or business). The application will generate a unique account number and password for your new account.

3. If you choose to sign in, you will need to enter your account number and password. If the credentials are valid, you will be logged in to your account.

4. Once logged in, you can perform various operations such as checking your account balance, depositing or withdrawing money, transferring funds to another account, or deleting your account.

5. All account data is stored in a text file named `accounts.txt` in the project directory. This file is read and updated whenever necessary.

## Dependencies

This application uses the following Python modules:

- `os`: Provides a way of using operating system dependent functionality.
- `json`: Implements JSON (JavaScript Object Notation), a lightweight data-interchange format.
- `random`: Contains functions for generating random numbers.
- `string`: Contains various string constants and classes, plus low-level operations on strings.

