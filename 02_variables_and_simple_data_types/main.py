#Variables
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)


#Strings
print("This is a string.") #Double Quotes
print('This is also a string.') #Single Quotes
text = """This is a long string
that spans multiple lines."""

name = "ada lovelace"
print(name.title())

# title() displays each word in titlecase, where each word begins with a
# capital letter. This is useful because you’ll often want to think of a name as a
# piece of information. For example, you might want your program to recognize
# the input values Ada, ADA, and ada as the same name, and display all of
# them as Ada.

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #Concatinate Strings
print(full_name)

# Python uses the plus symbol (+) to combine strings. In this example,
# we use + to create a full name by combining a first_name, a space, and a
# last_name

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")


#Adding Whitespace to Strings with Tabs or Newlines
#To add a tab to your text, use the character combination \t as shown:
print("\tPython")

#To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping Whitespace
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language.rstrip() #To Remove whitespaces from Right
favorite_language.lstrip() #To Remove whitespaces from left
favorite_language.strip()  #To Remove whitespaces from both sides


#Avoiding Syntax Errors with Strings
#The apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the string correctly
message = "One of Python's strengths is its diverse community."
print(message)

#However, if you use single quotes, Python can’t identify where the string should end and will give syntax error.
#For example, if you use an apostrophe within single quotes, you’ll produce an error. This happens because Python interprets
# everything between the first single quote and the apostrophe as a string. It then tries to interpret the rest
# of the text as Python code, which causes errors.
message = 'One of Python's strengths is its diverse community.'
print(message)

#Numbers
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

#Python use two multiplication symbols (**) to represent exponentiation, meaning "raise to the power of."
3 ** 2  # 3 to the power of 2 = 9
3 ** 3  # 3 to the power of 3 = 27
10 ** 6  # 10 to the power of 6 = 1,000,000

#Floats
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

#Avoiding Type Errors with the str() Function
age = 23
message = "Happy " + age + "rd Birthday!"
print(message) #It will give error as age is integer and remaining message is in string so we will convert the integer to string
# using str() function like given below
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#Comments
x = 10  # This is a comment
y = 20  # Python will ignore everything after the hash sign

# Using a backslash to continue the statement
total = 1 + 2 + 3 + \
        4 + 5 + 6
