class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initializing atributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer value to the given value
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")
            
    def increment_odometer(self, mileage):
        """Add the given amount to the odometer reading """
        self.odometer_reading += mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_discriptive_name())
#my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(14)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_discriptive_name())
my_used_car.update_odometer(20334)
my_used_car.read_odometer()
my_used_car.increment_odometer(20000)
my_used_car.read_odometer()