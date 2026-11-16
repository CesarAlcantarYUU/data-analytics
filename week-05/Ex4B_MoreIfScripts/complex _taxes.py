pay_rate = float(input(f"Enter your hourly pay rate: "))
hours_worked = float(input(f"Enter your hours worked: "))
filing_status = input("Enter filing status (single/joint): ")

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

annual_gross_pay = gross_pay * 52

print(f"Weekly Gross Pay: ${gross_pay:,.2f}")
print(f"Annual Gross Pay: ${annual_gross_pay:,.2f}")

if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay <75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay <25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    print("Invalid filing status")
    tax_rate = None

if tax_rate is not None:
    tax_withheld = gross_pay * tax_rate
    net_pay = gross_pay - tax_withheld

    print(f"You worked {hours_worked} hours this period.")
    print(f"Because you earn ${pay_rate:,.2f} per hour, your gross weekly pay is ${gross_pay:,.2f} ")
    print(f"Your annual gross pay is ${annual_gross_pay:,.2f}")
    print(f"Your filing status is {filing_status}")
    print(f"Your tax withholding for the week is ${tax_withheld:,.2f}")
    print(f"Your net pay is ${net_pay:,.2f}")