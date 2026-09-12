# Take home activity (1)
salary = float(input("Enter your salary: "))
rating = int(input("Enter your rating (1-4): "))
if rating == 1:
    bonus = salary * 0.2
elif rating == 2:
    bonus = salary * 0.15
elif rating == 3:
    bonus = salary * 0.10
elif rating == 4:
    bonus = salary * 0.05
else:
    bonus = 0
    print("invalid rating")
print("Bonus amount is:",bonus)


