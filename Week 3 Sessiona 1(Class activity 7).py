# Exer 7
#A college tutor wants a simple to store student information

print("Stdent Profile System")

student = {
"Name": input("Enter Student Name: "),
"Age": int(input("Enter Student Age: ")),
"Course": input("Enter Student Course: ")
}
paid = input("Has the student paid tuition fees? (yes/no:").lower()

if paid == "yes":
    student["fess_Paid"]= True
else:
    student["fess_Paid"] = False

for key, value in student.items():
    print(key)
    print(value)

