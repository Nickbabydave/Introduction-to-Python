# Exercise 1
number = int(input("Enter a number below 50: "))
for x in range(number, 51):
   print(x)

# Exercise 2
name = input("Enter your name")
number = int(input("Enter a number: "))
for x in range (number):
    print(name)
for letter in name:
    print(letter)

# Exercise 3
for number in range(1, 11):
    if number % 2 == 0:
        print("Even")
    else:
        print("odd")
