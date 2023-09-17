class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposit of {amount} successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account balance for {self.account_holder_name}: {self.account_balance}")


# Example usage
bank_account = BankAccount(12345, "John Doe", 1000)
bank_account.deposit(500)
bank_account.withdraw(200)
bank_account.display_balance()
