class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if amount < self.balance:
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        return self
    def display_account_info(self):
        # your code here
        print(self.balance)
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Account balance: {account.balance}, Interest rate: {account.int_rate}")

# account_1 = BankAccount(.01, 1000)
# account_2 = BankAccount(.01, 2100)

# # account_1.deposit(800).deposit(800).deposit(800).withdraw(2000).yield_interest().display_account_info()
# # account_2.deposit(1500).deposit(3500).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

# # BankAccount.print_all_accounts()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    # Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
    # your code here
        self.account.deposit(amount)
        print(f"Deposit of {amount} made. New balance is {self.bank_account.balance}")
    # Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        if self.bank_account.balance < amount:
            print("Insufficient funds.")
        else:
            self.account.withdraw(amount)
            print(f"Withdrawal of {amount} made. New balance is {self.bank_account.balance}")
    # Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.bank_account.balance}")

    # SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

    # SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

    # Submitting without bonuses but will com back to these...