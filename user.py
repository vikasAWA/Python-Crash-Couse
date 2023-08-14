class User():
    
    def __init__(self, first_name, last_name, age, location , occupation):
        """Initializing attributes of User"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
        print(f"Occupation: {self.occupation.title()}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")
        
    def increment_login_attempts(self):
        """Increment the login_attempts by 1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Reset the login attempts to 0"""
        self.login_attempts = 0

"""user_1 = User("john", 'doe', 20, 'newyork', 'software engineer')
user_1.describe_user()
user_1.greet_user()
user_2 = User("robert", 'parell', 40, 'San fransisco', 'manager')
user_2.describe_user()
user_2.greet_user()
"""

user = User("Ram", "jane", 23, "Delhi", "data analyst")
user.describe_user()
print(f"Login attempts: {user.login_attempts}")
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")