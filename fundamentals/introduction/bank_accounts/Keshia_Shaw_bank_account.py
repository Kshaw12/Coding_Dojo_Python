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


    #  def make_deposit(self, amount):
    #     if account == 'checking':
    #         self.account.deposit(amount)
    #         return self
    #     else:
    #         self.saving.deposit(amount)
    #         return self
bob= BankAccount(.20, 100) 
amy= BankAccount(.0000001, 5000000)

bob.make_deposit(1)
bob.make_deposit(100)
bob.make_deposit(177777)
bob.make_withdraw(50)
bob.display_user_balance()
bob.yield_interest()
bob.display_user_balance()

amy.make_deposit(20)
amy.make_deposit(40)
amy.make_withdraw(5)
amy.make_withdraw(10)
amy.make_withdraw(5)
amy.make_withdraw(7)
amy.display_user_balance()
amy.yield_interest()
amy.display_user_balance()



