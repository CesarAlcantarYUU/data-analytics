
# Cesar Alcantar
# 3B Exercise More Classes

class Restaurant:
    """A class that describes different restaurants and the food they serve."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers were served today? "))
        self.number_served += customers

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            try:
                rating = float(input("Rate your experience from 1-5: "))

                if rating.is_integer() and 1 <= rating <= 5:
                    rating = int(rating)
                    self.customer_ratings.append(rating)

                    average = sum(self.customer_ratings) / len(self.customer_ratings)

                    print(f"Your rating was {rating}.")
                    print(f"The average rating is {average:.1f}.")
                    break

                else:
                    print("Invalid rating. Please enter a whole number between 1 and 5.")

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                
# Create restaurant objects

restaurant1 = Restaurant("In-N-Out Burger", "Burgers")
restaurant2 = Restaurant("Taco Bell", "Mexican food")
restaurant3 = Restaurant("Dunkin' Donuts", "Coffee and donuts")

# Restaurant 1

restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.add_num_served()
restaurant1.print_num_served()
restaurant1.customer_rating()

# Restaurant 2

restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.add_num_served()
restaurant2.print_num_served()
restaurant2.customer_rating()

# Restaurant 3

restaurant3.describe_rest()
restaurant3.rest_open()
restaurant3.add_num_served()
restaurant3.print_num_served()
restaurant3.customer_rating()
