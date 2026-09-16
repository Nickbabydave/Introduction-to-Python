# Small school library keep track of books that students borrow.
# Exe 8

book = {
"title" :input("Enter book title:"),
"author" : input("Enter book author:"),
"year" : int(input("Enter book year:")),
"available": True
}
print(book)
book["available"] = False
print(book)

student["age"] =30
book["available"] = False

# This book is borrowed, so availability is changed from True to False.
# Error: NameError because the variable name book was not defined.


