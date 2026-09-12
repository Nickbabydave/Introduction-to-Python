# Take Home Activity 2
income = float(input("Enter your annual income: "))
allowance = 12570

if income <= allowance:
    tax = 0

elif income <= 50250:
    taxable_income = income - allowance
    tax = taxable_income * 0.20

elif income <= 125140:
    basic_tax = (20250 - allowance) * 0.20
    higher_tax = (income - 50250) *0.40
    tax = basic_tax + higher_tax

else:
    basic_tax = (50250 - allowance) * 0.20
    higher_tax = (125140 - 50250) * 0.40
    additional_tax = (income - 125140) * 0.45
    tax = basic_tax + higher_tax + additional_tax
print("Total income tax is £:", tax)

