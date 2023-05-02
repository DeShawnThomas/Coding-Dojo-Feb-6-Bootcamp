class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards member:", self.is_rewards_member)
        print("Gold card points:", self.gold_card_points)


# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
re
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Price deduction too large.")

new_user1 = User("DeShawn", "Thomas", "deshawnxthomas@gmail.com", 27)
# new_user1.display_info()

# Enrolling the user and then displaying the user's information.
new_user1.enroll()
new_user1.display_info()

new_user2 = User("Sarah", "Edens", "sarahedens07@gmail.com", 26)
new_user3 = User("Tony", "Francois", "tonyfrancois22@gmail.com", 27)

new_user2.enroll()
new_user2.spend_points(50)
new_user2.display_info()

new_user3.enroll()
new_user3.spend_points(80)
new_user3.display_info()