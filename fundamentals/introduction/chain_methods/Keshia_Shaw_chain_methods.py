#the class
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate= int_rate
        self.balance= balance

# Methods***********
    def make_withdraw(self, amount):
        self.balance= self.balance - amount

    def yield_interest(self):
        self.balance= self.balance * self.int_rate

     def make_deposit(self, amount):
        if account == 'checking':
            self.account.deposit(amount)
            return self
        else:
            self.saving.deposit(amount)
            return self
    def display_user_balance(self):
        print(f'Hello. Your current balance is {self.balance}.')     

bob= BankAccount(.20, 100) 
amy= BankAccount(.0000001, 5000000)


# non-Chain Methond**********
# user1.display_info()
# user1.enroll()
# user1.spend_points(50)
# user1.display_info()
# user2.enroll()
# user2.spend_points(80)
# user2.display_info()

# ****Chain Method*******
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()


   