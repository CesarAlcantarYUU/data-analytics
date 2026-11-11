# How do you calculate the area of a circle?
import math

diameter = 22
radius = diameter / 2

area = math.pi * radius ** 2

print(f'The area of a circle with radius {radius} is {area:,.2f}')

# I like using f strings when dealing with more than one variable in a print statement. It makes it easier to read and understand what is being printed.