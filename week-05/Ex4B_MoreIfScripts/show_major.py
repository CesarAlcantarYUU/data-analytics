student_name = input(f"Enter Student Name: ")
student_major = input(f"Enter Major Code: ")

if student_major == "BIOL":
    major_name = "Biology"
    department_name = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    department_name = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    department_name = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    department_name = "Kerr Hall, Room 114"
elif  student_name == "MKT":
    major_name = "Marketing"
    department_name = "Westly Hall, Room 310"
else:
    major_name = "<unknown>"
    department_name = ""

print("Student Name:", student_name)
print("Student Major Code:", student_major)
print("Student Major Name:", major_name)
print("Department Location:", department_name)