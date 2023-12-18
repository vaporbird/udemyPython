class User:
	def __init__(self, user_id, username):
		print("new user being created")
		self.hair_color = "blue"
		self.id = user_id
		self.username = username.capitalize()
	def change_hair(self, color):
		self.hair_color = color

user1 = User("001", "ivan")
print(user1.hair_color)
print(user1.id)
print(user1.username)
user1.change_hair("white")
print(user1.hair_color)
