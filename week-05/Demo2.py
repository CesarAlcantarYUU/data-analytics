item1 = 25.75
item2 = 45.67
item3 = 45.75
item4 = 55.67
item5 = 45.60

sub_total = item1 + item2 + item3 + item4 + item5

tax = 0.07 * sub_total
TotalCost = sub_total + tax

print(f'TotalCost: ${TotalCost:.2f}')
print(f'      Tax: ${tax:.2f}')
print(f'Subtotal: ${sub_total:.2f}')