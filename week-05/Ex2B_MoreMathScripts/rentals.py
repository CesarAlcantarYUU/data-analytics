# Rental Price Calculator
import math
tourist = 38
van_seats = 15
van_cost = 250
vans_needed = math.ceil(tourist / van_seats)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / tourist

print(f"Total vans needed: {vans_needed}")
print(f"Total rental cost: ${total_cost}")
print(f"Cost per person: ${cost_per_person:.2f}")

# script says I need to charge $19.74 per person.
# If I multiply it out I get $750.12.
# The vans in total cost $750.
# I have left over $0.12 because the function math.ceil() rounded up the amount charged per person.