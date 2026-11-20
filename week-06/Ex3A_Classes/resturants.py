# Cesar Alcantar
# 3A Exercise Resturants

class Restaurant:
    """A class that describes different restaurants and the food they serve."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")



restaurant1 = Restaurant("In-N-Out Burger", "Burgers")

restaurant2 = Restaurant("Taco Bell", "Mexican food")

restaurant3 = Restaurant("Dunkin' Donuts", "Coffee and donuts")


restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()
