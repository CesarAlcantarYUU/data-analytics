sales_data = [
    ('Marcus Webb',    'East', 4250.00),
    ('Priya Sharma',   'West', 5875.50),
    ('Deshawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen',      'West', 4980.25),
]

for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")