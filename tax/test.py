import mod

income = float(input("Enter annual income: "))
jury = input("Are you on jury service (y/n): ")

#Call functions from mod.py
if income <= 85_528:
    tax = mod.low_tax(income, jury)
elif income < 85_528:
    tax = mod.high_tax(income, jury)
#If under 0 then no tax paid or rebates
if tax < 0:
    tax = 0

print(f"The tax is, {tax} thalers.")

