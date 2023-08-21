from car import ElectricCar, Car

my_beetle = Car('Volkswebgan', 'beetle', 2012)
my_tesla = ElectricCar('tesla', 'roadster', 2022)

print(my_beetle.get_discriptive_name())
print(my_tesla.get_discriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()