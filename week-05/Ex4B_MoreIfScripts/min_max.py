a = 2
b = 4
c = 6

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Finding the largest value

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The smallest number is:", smallest)
print("The largest number is:", largest)