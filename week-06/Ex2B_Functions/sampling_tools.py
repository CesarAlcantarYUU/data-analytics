import random

products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]
product_of_the_day = random.choice(products)

print("PRODUCT OF THE DAY")
print(product_of_the_day)

selected_products = random.sample(products, 3)

print("\nPRODUCTS SELECTED FOR SURVEY")
print(selected_products)

random.shuffle(products)

print("\nPRODUCTS IN RANDOM ORDER")
print(products)

transactions = random.randint(50, 300)

print("\nDAILY TRANSACTION COUNT")
print(transactions)