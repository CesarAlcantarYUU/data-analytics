candy_types = ("skittles", "starburst", "jollyranchers")
fruity_flavors = ("strawberry", "orange", "lemon")

candy_combinations = {
    candy_types[0] + " " + fruity_flavors[1],
    candy_types[1] + " " + fruity_flavors[0],
    candy_types[2] + " " + fruity_flavors[2]
}

print("Todays candy options include:")
print(candy_combinations)
print(candy_combinations)
print(candy_combinations)

# I noticed that the items print out in a different order.