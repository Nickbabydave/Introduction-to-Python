# Create Dictionary with user input person
person1 = {
"Name": input("Enter your name: "),
"Age" : int(input("Enter your age: "))
}
person2 = {
"Course": input("Enter your course: "),
"Address" : input("Enter your address: ")
}

combined = person1 | person2
print(combined)

