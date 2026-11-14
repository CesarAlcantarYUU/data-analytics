contact_info = {
    "Name": "Josh",
    "Address": "455 Lasuen st",
    "City": "San Jose",
    "State": "California",
    "Zip": "94071"
}
print(f"""{contact_info["Name"]}
{contact_info["Address"]}
{contact_info["City"]}, {contact_info["State"]}, {contact_info["Zip"]}""")

contact_info.pop("Name")

print() 

full_name = {
    "first name": "Josh",
    "last name": "Allen"
}

full_name.update({"honorific": "Mr."})

contact_info.update(full_name)

print(f"""{contact_info["honorific"]} {contact_info["first name"]} {contact_info["last name"]}
{contact_info["Address"]}
{contact_info["City"]}, {contact_info["State"]}, {contact_info["Zip"]}""")