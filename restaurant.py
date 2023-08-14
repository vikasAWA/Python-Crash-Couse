class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Describing restaurant"""
        print(f"Name of restaaurant is {self.restaurant_name.title()}.\nCuisine Type is {self.cuisine_type.title()}.\n")
    
    def open_restaurant(self):
        """Printing mesage indicating the status of restaurant open or not"""
        print(f"{self.restaurant_name.title()} is open.\n")
        
    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can not decrease the number of peple served. !")
            
    def increment_number_served(self, number):
        """Add the given number to the existing number number served"""
        if number >= 0:
            self.number_served += number
        
restaurant = Restaurant("Delhi food express", "North Indian food")
#print(restaurant.restaurant_name)
#print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""restaurant_1 = Restaurant("Chennai Foods", "South indian")
restaurant_2 = Restaurant("Punjabi Dhaba", "north Indian")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()"""

print(f"Number of Customer Served : {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number of Customer Served : {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Number of Customer Served : {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Number of Customer Served : {restaurant.number_served}")