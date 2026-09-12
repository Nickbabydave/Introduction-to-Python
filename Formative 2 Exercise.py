# FORMATIVE 2 EXERCISE
# Ex - 1 (Conditional Statements)
# Favourite colour

# colour = input("Enter a favourite colour: ")
# if colour in ["red", "RED", "Red"]:
#     print("I like red too")
# else:
#     print("I prefer red", colour, "i don't like")

# Ex - 2
# Menu option

# print("1. Add")
# print("2. Search")
# print("3. Update")
# print("4. Delete")
#
# number = int(input("enter a number between 1 and 4: "))
#
# if number == 1:
#     print("Added")
# elif number == 2:
#     print("Searched")
# elif number == 3:
#     print("Updated")
# elif number == 4:
#     print("Deleted")
# else:
#     print("Goodbye")

# Ex - 3
# Temperature between Celsius and kelvin

# print("1. Celsius to kelvin")
# print("2. Kelvin to Celsius")
# choice = int(input("Choose 1 or 2: "))
# if choice == 1:
#     celsius = float(input("Enter Celsius: "))
#     kelvin = celsius + 273.15
#     print("kelvin is ", kelvin)
#
# elif choice == 2:
#     kelvin = float(input("Enter Kelvin: "))
#     celsius = kelvin - 273.15
#     print("Celsius is ", celsius)
# else:
#     print("Invalid choice")

# LOOP
# Ex - 4
# Number from 1 to 10 but skip even number

# for number in range(1, 11):
#     if number % 2 != 0:
#        print(number)

# Ex - 5
# Print each letter except H using continue

# word = "PYTHON"
#
# for letter in word:
#     if letter == "H":
#         continue
#     print(letter)

# Ex - 6
# Keep asking until user enters exit

# word = input("Enter a word: ")
#
# while word != "exit":
#     word = input("Enter another word: ")
# print("Program stopped")

# Ex - 7
# Count up  or down

direction = input("Enter up or down: ")
if direction == "up":
    number = int(input("Enter the top number: "))
    for a in range(1, number + 1):
        print(a)

elif direction == "down":
    number = int(input("Enter a number below 20: "))
    for a in range(20, number - 1, -1):
        print(a)
else:
    print("I did not understand")

