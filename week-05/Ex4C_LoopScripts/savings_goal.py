bank_balance = float(input(f"Enter your starting bank balance: "))
savings_goal = float(input(f"Enter your savings goals: "))
weekly_savings = float(input(f"Enter your weekly savings amount: "))

treat_purchased = False

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings
print(f"This week my balance increased to", bank_balance)

if bank_balance > savings_goal / 2:
    print(f"Alomost there! This week my balance went up to", bank_balance)
    if bank_balance >= savings_goal * 0.75 and not treat_purchased:
        bank_balance = bank_balance - 10
        treat_purchased = True

        print("So close! After treating myself, my my balance is up to", bank_balance)
print("Goal met! My current bakance is", bank_balance)