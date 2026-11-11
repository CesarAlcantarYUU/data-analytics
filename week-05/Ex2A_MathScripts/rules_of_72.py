# Rule of 72
savings = 5000
rate_of_return = 0.08  # 8% annual return
years_to_double = 72 / (rate_of_return * 100)

print(f"Your current savings is ${savings: ,.2f}")
print(f"At a {rate_of_return:.0%} interest rate, your savings account will be worth \
${savings * 2: ,.2f} in {years_to_double:.1f} years.")