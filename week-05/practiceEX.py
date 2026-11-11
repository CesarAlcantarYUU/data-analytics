meal = float(input('Enter the cost of the meal: $'))

Tip = .20 * meal
Tax = .0825 * meal
TotalCost = meal + Tip + Tax

print(f'----- Meal Cost Breakdown -----')
print(f'Subtotal:       ${meal:.2f}')
print(f'Tip (20%):      ${Tip:.2f}')
print(f'Tax (8.25%):    ${Tax:.2f}')
print(f'--------------------------------')
print(f'Total:          ${TotalCost:.2f}')