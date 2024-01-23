class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate= int_rate
        self.balance= balance

    
    # def withdraw(self, amount):
    def make_withdraw(self, amount):
        self.balance= self.balance - amount


        # ***********Deposit*****************************************
    def make_deposit(self, amount):
        self.balance= self.balance + amount
   
# **********************display accoutn************************
    
    def display_user_balance(self):
        print(f'Hello. Your current balance is {self.balance}.')     


    def yield_interest(self):
        self.balance= self.balance * self.int_rate
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate= int_rate
        self.balance= balance

    
    # def withdraw(self, amount):
    def make_withdraw(self, amount):
        self.balance= self.balance - amount


        # ***********Deposit*****************************************
    def make_deposit(self, amount):
        self.balance= self.balance + amount
   
# **********************display accoutn************************
    
    def display_user_balance(self):
        print(f'Hello. Your current balance is {self.balance}.')     


    def yield_interest(self):
        self.balance= self.balance * self.int_rate



class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account_balance= account_balance
    # other methods
    
    def make_deposit(self, amount):
            self.account_balance= self.account_balance + amount
 
    def make_withdraw(self, amount):
        self.balance= self.balance - amount

    def balance(self, deposit, account_balance):
        self.account.deposit(100)
    	print(self.account_balance)



