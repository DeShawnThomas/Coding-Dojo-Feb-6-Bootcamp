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

account_1 = BankAccount(.01, 1000)
account_2 = BankAccount(.01, 2100)

account_1.deposit(800).deposit(800).deposit(800).withdraw(2000).yield_interest().display_account_info()
account_2.deposit(1500).deposit(3500).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

BankAccount.print_all_accounts()