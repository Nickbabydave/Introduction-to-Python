#Conditional Statements Exercises
#Student's grade based on given input marks
#Ex - 1

number = int(input("Enter your marks"))
if number < 0 or number > 100:
    print("Invalid marks")

if number > 75:
    print("Distinction")

elif number >= 60 and number <= 74:
    print("Merit")

elif number >= 40 and number <= 59:
    print("Pass")

elif number >= 0 and number <= 39:
    print("Fail")

else:
    print("Fail")

#Ex - 2
#calculate the number of characters from a user's string input)

word = input("enter a word:")
characters = len(word)

if characters == 0:
    print("You didn't type anything")

elif characters <= 3:
    print("Too short word")

elif characters <= 8:
    print("Small word")

elif characters <= 12:
    print("Big word")

else:
    print("Too big word")

print("Number of characters:", characters)

#Ex - 3
#Display hourly rate for 4 different professions

profession = input("enter your profession: ")

if  profession == "Teacher":
    print("Hourly rate is £25")

elif profession == "Doctor":
    print("Hourly rate is £60")

elif profession == "Lawyer":
    print("Hourly rate is £200")

elif profession == "Driver":
    print("Hourly rate is £15")

else:
    print("Profession not found")

#Ex - 4
#To add two numbers

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if num1. isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    total = num1 + num2

    if total < 100:
       print("The total is less than 100")
    else:
       print("The total is 100 or more")
else:
    print("Please enter number only")

#Ex - 5
#fruit and vowels

fruit = input("Enter fruit name: ").lower()

if fruit[0] in "aeiou":

    if fruit[1] in "aeiou":
        print("Both first and second letters are vowels")
    else:
        print("Only first letter is a vowel")
else:
    print("The first letter is not a vowel")

# Ex - 6
#Range and odd/even

number = int(input("Enter a number: "))

if number >= 0 and number <= 100:

    if number % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
else:
    print("The number is not within the range")

#Loop Exercise
#Print all fruits accepts banana
#Ex - 7

fruits = ["orange", "banana", "apple", "pear"]

for fruit in fruits:
    if fruit != "banana":
        print(fruit)

# Ex - 8
# Secret number guessing

secret_number = 7

guess = int(input("Guess the secret number: "))
while  guess !=  secret_number:
    print("wrong, try again")
    guess = int(input("Guess again: "))
print("You guessed the secret number")

# Ex - 9
# Name and number

name = input("What is your name? ")
number = int(input("Enter a number: "))

if number < 10:
    for a in range(number):
        print(name)
else:
    for a in range(3):
        print("Too high")


















