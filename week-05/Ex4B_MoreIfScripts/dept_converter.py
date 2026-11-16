dept_code = int(input(f"Enter department code: "))
if dept_code == 1:
    print("Marketing")
elif dept_code == 5:
    print("Human Resources")
if dept_code == 10:
    print("Accounting")
elif dept_code == 12:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")

else:
    print("Invalid Department Code")

dept_code = int(input(f"Enter department code: "))

match dept_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code")

# I think in the future I will be using the "match / case" statement. Just because it looks a lot cleaner and easier to read.
