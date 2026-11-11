# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown
total_due = food_cost + tax + tip
# Display the results
# print("The total due is " + str(total_due))

# the str() function is being used here to convert the numeric value of total_due into
# a string so that it can be concatenated with the other string in the print statement.
# Without this conversion, Python would raise a TypeError because it cannot concatenate a
# string and a float directly.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Total due is " + str(total_due))
print("Tip is " + format(tip, ".2f"))