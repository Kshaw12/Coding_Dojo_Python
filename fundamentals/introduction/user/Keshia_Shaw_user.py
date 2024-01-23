#the class
class User:
    #the constructor
    def __init__ (self, first_name, last_name, email, age, is_rewards_member= False, gold_card_points= 0):
        #the attributes
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.age= age
        self.is_rewards_member= is_rewards_member
        self.gold_card_points = gold_card_points

    #method
    def greet (self):
        print("hello, my name is {self} and my age is {.age}!'")

#*********************Display info on Seperate lines*************************************************
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: { self.last_name}")
        print(f"Email: { self.email}")
        print(f"Age: {self.age}")
        print(f"Is a rewards member? {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend(self, amount):
        self.gold_card_points= self.gold_card_points- amount

# below me is outside of the class************************************
user1 = User("John", "Doe", "jdoe@gmail.com", 18)

print(user1.is_rewards_member)
user1.display_info()
user1.enroll()
user1.display_info()
user1.spend(150)
user1.display_info()
#***************************************************************************************************
#enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
#senroll(self)


#***spend_points(self, amount) - have this method decrease the user's points by the amount specified.**************