"""
# ------ Pretty Table ----------
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
# ------- End ----------------
"""

# ------- Classes ------------
# first:
"""
class User:
    pass


user_1 = User()
user_1.id = "001"
user_1.name = "angel"

print(user_1.name)

user_2 = User()
user_2.id = "002"
user_2.name = "jack"
"""


# second

class User:
    def __init__(self, user_id, username):
        print("User being created")
        self.id = user_id
        self.username = username
        self.followers = 0  # this is default value
        self.following = 0  # this is default value

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angel")
user_2 = User("002", "Jack")

print(user_1.id)
print(user_1.username)
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)