class User():
    
    def __init__(self, first_name, last_name, age, location , occupation):
        """Initializing attributes of User"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.location = location
        self.occupation = occupation
        
    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
        print(f"Occupation: {self.occupation.title()}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")
        
user_1 = User("john", 'doe', 20, 'newyork', 'software engineer')
user_1.describe_user()
user_1.greet_user()
user_2 = User("robert", 'parell', 40, 'San fransisco', 'manager')
user_2.describe_user()
user_2.greet_user()