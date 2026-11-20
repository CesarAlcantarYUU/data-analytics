def display_mailing_label(name, address, city, state, zip):  
    print(f"{name}\n{address}\n{city}, {state} {zip}")


def add_numbers(*numbers): 
    total = sum(numbers)
    expression = " + ".join(str(number) for number in numbers)  
    print(f"{expression} = {total}")


def display_receipt(total_due, amount_paid):  
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}\n")
    if amount_paid < total_due:
        print(f"Remaining Balance: ${total_due - amount_paid:.2f}")
    else:
        print(f"Change Due: ${amount_paid - total_due:.2f}")


display_mailing_label("Cesar Alcantr", "123 Cesar Street", "San jose", "CA", "94987")
print()
display_mailing_label("Ramon Ochoa", "098 Jack ave", "San Francisco", "CA", "94892")
print()
add_numbers(5)
add_numbers(5, 8)
add_numbers(5, 8, 12, 20)
print()
display_receipt(25.50, 30.00)
print()
display_receipt(25.50, 25.50)
print()
display_receipt(25.50, 20.00)