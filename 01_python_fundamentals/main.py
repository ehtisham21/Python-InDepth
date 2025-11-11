#Python was created by Guido van Rossum in the late 1980s and was first released in 1991


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


#Keywords
#Keywords are reserved words in Python that have special meanings and cannot be used as regular identifiers (like variable names or function names).
#Python v2 has 31 keywords.
#Python v3 has 35 keywords.
#New keywords in Python v3 include False, None, True, and nonlocal



#Operators
#Operators are non-alphanumeric characters and combinations of characters that Python uses to perform operations on data.

# Arithmetic Operators ➕➖✖️➗
#Comparison Operators  < > = <= >= !=
#Bitwise Operators in Python (Bitwise operators in Python operate on the binary representations of numbers, allowing you to perform operations at the bit level)
# & : Bitwise AND
# | : Bitwise OR
# ^ : Bitwise XOR (Exclusive OR)
# ~ : Bitwise NOT (One’s Complement)
# << : Left Shift
# >> : Right Shift
#Assignment Operators  =, +=, -=, *=, /=, //=, %= , **=
#Logical Operators and, or, not
#Membership Operators in, not in
#Identity Operators is, is not



#DataTypes
#Mutable vs Immutable:
#Mutable Objects: These are objects that can be changed after they are created. For example, lists and dictionaries (which we are not covering here).
#Immutable Objects: These are objects that cannot be changed once they are created. For example, integers, floats, strings, and tuples.
# Type Checking in Python:
# Python provides two built-in functions to check the type of an object:
# type(obj): Returns the type of the object obj.
# isinstance(obj, type): Returns True if obj is an instance of type or class or any subclass.
# x = 42
# print(type(x))  # Output: <class 'int'>
# print(isinstance(x, int))  # Output: True
#Numeric Data Types int, float, complex
#String Type, Boolean Type

# Examples of imaginary literals
print(0j, 0.j, 0.0j, .0j, 1j, 1.j, 1.0j, 1e0j, 1.e0j, 1.0e0j)

# Complex numbers
print(1+0j, 1.0+0.0j)