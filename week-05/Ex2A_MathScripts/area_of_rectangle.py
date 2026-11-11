# Calculating area of rectangle
SideA = float(input("Enter the length of side A: "))
SideB = float(input("Enter the length of side B: "))

Area = SideA * SideB

print("Side A is", SideA)
print("Side B is", SideB)
print("The area of the rectangle is", Area)

# pitfalls is that I have input my values in the output terminal in order for it to work. I also had to make sure that I used the float() function in order for it to work properly. If I did not use the float() function, it would not have worked because it would have been a string and not a number.