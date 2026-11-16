pay_rate = float(input(f"Enter your hourly pay rate: "))
hours_worked = float(input(f"Enter your hours worked: "))

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

print(f"Gross Pay: ${gross_pay:.2f}")