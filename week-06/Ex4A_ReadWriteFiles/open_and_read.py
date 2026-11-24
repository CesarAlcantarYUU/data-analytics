f = open("about_me.txt", "r")


# print(f.read()) prints out all characters

# print(f.read(50)) only prints out 50 characters

# print(f.readline(10))
# print(f.readline())

# for i in range(1, 5):
#     print(f.readline())

# print(f.readlines(1)) displays all lines
# print(f.readlines(1)) displays only first line
# print(f.readlines(10)) displays only first line
# print(f.readlines(100)) displays only some lines
# print(f.readlines(-1)) displays all lines


# First variable: Read the first 50 characters
first_variable = f.read(50)

# Second variable: Capture the next four lines
second_variable = []

for i in range(1, 5):
    second_variable.append(f.readline())

# Third variable: Read the next 100 characters
third_variable = f.readlines(100)


print("First 50 characters:", first_variable)
print("Next four lines, as list by line:", second_variable)
print("Next 100 characters, as list by line, rounded up to complete lines:",
      third_variable)

f.close()
