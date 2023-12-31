class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initializing name and age attributes."""
        self.name = name 
        self.age = age 
        
    def sit(self):
        """Simulating a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")
        
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " is rolled over")
        
my_dog = Dog('zimmi', 13)
print(f"My dog name is {my_dog.name.title()}.")
print(f"My dog age is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 6)
print(f"\nYour dog name is {your_dog.name.title()}")
print(f"Your dog age is {your_dog.age} years old.")
your_dog.sit()