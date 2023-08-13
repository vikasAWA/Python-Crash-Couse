class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Describing restaurant"""
        print(f"Name of restaaurant is {self.restaurant_name.title()}.\nCuisine Type is {self.cuisine_type.title()}.\n")
    
    def open_restaurant(self):
        """Printing mesage indicating the status of restaurant open or not"""
        print(f"{self.restaurant_name.title()} is open.\n")
        
restaurant = Restaurant("Delhi food express", "North Indian food")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("Chennai Foods", "South indian")
restaurant_2 = Restaurant("Punjabi Dhaba", "north Indian")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()