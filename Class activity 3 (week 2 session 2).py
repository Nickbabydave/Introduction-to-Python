#Example  Exercise 1
# Calculate sum of numbers until user enters 0
# total = 0
# number = int(input("Enter a number(0 to stop):"))
# while number != 0:
#     total = total + number
#     number = int(input("Enter a number(0 to stop):"))
#     print("The total is" , total)

#Example Exercise 2
number = int(input("Enter a number between 15 and 25: "))
while number < 10 or number > 20:
    if number < 10:
        print("Too low")
    else:
        print("Too high")
    number = int(input("Try again"))
print("Thank You")

# Exercise 3



