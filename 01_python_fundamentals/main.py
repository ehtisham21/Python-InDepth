x = 10  # This is a comment
y = 20  # Python will ignore everything after the hash sign


# Using a backslash to continue the statement (Create multiple lines in to single line.)
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Using parentheses to continue the statement (Create multiple lines in to single line.)
total = (1 + 2 + 3 +
         4 + 5 + 6)


text = """This is a long string
that spans multiple lines."""


if x > 0:
    print("Positive number")
    y = x
else:
    print("Non-positive number")
    y = 0

def greet(name):
    print(f"Hello, {name}!")  # Correct: 4 spaces for indentation

#Tokens as identifiers (how Python processes each line of code by breaking it down into basic components known as tokens)
# Incorrect: Python would parse 'ifx' as a single identifier
ifx = 10

# Correct: Adding whitespace to separate 'if' and 'x'
if x == 10:
    print("x is 10")

# Here, Python breaks it into tokens:
# x → identifier (a name)
# = → operator
# 10 → literal (a fixed value)


#Identifiers(An identifier is a name used to specify a variable, function, class, module, or any other object in Python.)
my_variable = 10  # Valid identifier
MyVariable = 20   # Another valid identifier (different from the first due to case sensitivity)
1stVariable = 30  # Invalid identifier (cannot start with a digit)
hello1 = 5
hello2  = 10
result = hello1+hello2
print(result)



class MyClass:  # Class name starts with an uppercase letter
    pass

def my_function():  # Function name starts with a lowercase letter
    pass

#Private Identifiers
#Starting an identifier with a single leading underscore _ indicates that the identifier is intended to be private.
#Starting with two leading underscores __ indicates a strongly private identifier.
#If an identifier starts and ends with double underscores __name__, it is a language-defined special names or also called dunder names
_private_var = 10  # Indicates a private variable
__strong_private_var = 20  # Indicates a strongly private variable
__init__ = 30  # Special language-defined name (used in class constructors)


