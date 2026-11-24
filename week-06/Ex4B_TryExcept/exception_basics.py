try:
    number = int("hi")
except ValueError:
    print("You entered a value that cannot be converted into an number.")
else:
    print("The number is:", number)
finally:
    print("Let's try another one.")

try:
    print(x)
except NameError:
    print("This variable has not been defined.")
else:
    print("This variable is:", x)
finally:
    print("Let's try another one.")

try:
    result = "hi" + 10
except TypeError:
    print("You cannot combine a string and an integer this way.")
else:
    print("The result is:", result)
finally:
    print("Let's try another one.")

try:
    exec("print('hi'")
except SyntaxError:
    print("There is a syntax error in the code.")
else:
    print("The code executed successfully.")
finally:
    print("Let's try another one.")