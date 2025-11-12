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
# Imaginary literals are created by appending j or J to a floating-point or decimal literal.
# Complex numbers
print(1+0j, 1.0+0.0j)
# Complex numbers are numbers that have a real part and an imaginary part. In Python, they are represented as a + bj, where a is the real part, and b is the imaginary part.


# Variables as references
x = 42       # x is a reference to an integer object
x = "hello"  # x is now a reference to a string object
x = 10    # Binding: x is now a reference to the integer 10
x = 20    # Rebinding: x is now a reference to the integer 20
x = 10    # x is bound to the integer 10
del x     # x is unbound, and the name x no longer exists
x = [1, 2, 3]  # x is bound to a list object
y = x          # y is also bound to the same list object
del x          # x is unbound, but the list object still exists because y refers to it



#If elif else
our_age = 12

if our_age < 4:
    print("Your admission cost is $0.")
elif our_age < 18:
    print("Your admission cost is $25.")
else: # else will only work when all the other conditions are false.
    print("Your admission cost is $40.")

#Iterations or Loops
#An iteration refers to a single pass or repetition through the body of the loop. Essentially, every time the loop executes, it's called an iteration.
# Loops are fundamental concepts in programming that allow you to execute a block of code multiple times.
#for loop, while loop
#Break Statement
# Terminates the loop's execution and transfers control to the statement following the loop.
# Continue Statement
# Skips the current iteration of the loop. The remaining code in the loop body is not executed for that iteration.
# Pass Statement
# Used when a statement is syntactically required but no code needs to be executed. Useful as a placeholder.
# range()
# The built-in range() function is commonly used with loops to generate a sequence of numbers:
# Syntax: range(start, stop, step)
# start: The starting value (default is 0).
# stop: The stopping value (not included in the sequence).
# step: The difference between each number in the sequence (default is 1
print(list(range(10)))        # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(4, 9)))      # Output: [4, 5, 6, 7, 8]
print(list(range(5, 25, 4)))  # Output: [5, 9, 13, 17, 21]


#Strings
# Using single quotes
str1 = 'Hello Python'
print(str1)  # Output: Hello Python

# Using double quotes
str2 = "Hello Python"
print(str2)  # Output: Hello Python

# Using triple quotes
str3 = '''Triple quotes are generally used for
multiline strings or docstrings.'''
print(str3)

# Strings Indexing and Splitting
str = "HELLO"

# Positive indexing
print(str[0])  # Output: H
print(str[1])  # Output: E

# Negative indexing
print(str[-1])  # Output: O
print(str[-2])  # Output: L


# String Methods
# Common String Methods:
# capitalize(): Converts the first character to uppercase.
# lower(): Converts the entire string to lowercase.
# upper(): Converts the entire string to uppercase.
# find(): Searches the string for a specified value and returns the position of where it was found.
# replace(): Returns a string where a specified value is replaced with another value.

str = "hello world"
# Capitalize the first letter
print(str.capitalize())  # Output: Hello world
# Convert to uppercase
print(str.upper())  # Output: HELLO WORLD
# Find a substring
print(str.find("world"))  # Output: 6
# Replace a substring
print(str.replace("world", "Python"))  # Output: hello Python
# String Indexing and Slicing
word = 'Didcoding'

# Accessing individual characters
print(word[0])  # Output: D
print(word[5])  # Output: d

# Slicing
print(word[0:2])  # Output: Di
print(word[2:5])  # Output: dco
print(word[::-1])  # Output: gnidcoDid (Reversed string)

# StringOperators
str1 = "Hello"
str2 = " World"
# Concatenation
print(str1 + str2)  # Output: Hello World
# Repetition
print(str1 * 3)  # Output: HelloHelloHello
# Membership
print('H' in str1)  # Output: True



# Use isdigit():
# Use isdigit() when you want to check if a string contains numeric characters, including digits from other numeral systems such as Arabic digits, superscript digits, or any other non-decimal characters that represent numbers.
# Example 1: Regular decimal digits
s1 = "12345"
print(s1.isdigit())  # True (all characters are base-10 digits)
# Example 2: Arabic numerals
s2 = "٢٣"  # Arabic digits for 23
print(s2.isdigit())  # True (Arabic digits are considered digits in `isdigit()`)
# Example 3: Superscript digits
s3 = "²³"  # Superscript digits
print(s3.isdigit())  # True (superscript digits are considered valid digits)
# Example 4: Non-numeric characters included
s4 = "123abc"
print(s4.isdigit())  # False (contains alphabetic characters)
# Example 5: Mixed with spaces
s5 = " 123 "
print(s5.isdigit())  # False (contains spaces)

# Use isdecimal():
# Use isdecimal() when you want to check if a string consists only of decimal digits (0-9) in the base-10 number system. This is more restrictive than isdigit(), as it only accepts the digits used in everyday counting (i.e., 0–9), and it does not accept digits from other numbering systems.
# Example 1: Regular decimal digits
s1 = "12345"
print(s1.isdecimal())  # True (all characters are base-10 digits)
# Example 2: Arabic numerals
s2 = "٢٣"  # Arabic digits for 23
print(s2.isdecimal())  # False (Arabic numerals are not considered decimal digits)
# Example 3: Superscript digits
s3 = "²³"  # Superscript digits
print(s3.isdecimal())  # False (superscript digits are not considered decimal digits)
# Example 4: Non-numeric characters included
s4 = "123abc"
print(s4.isdecimal())  # False (contains alphabetic characters)
# Example 5: Mixed with spaces
s5 = " 123 "
print(s5.isdecimal())  # False (contains spaces)
# You can think of isnumeric() as a superset of isdigit(). It includes all the functionality of isdigit() but adds additional support for other numeric characters that isdigit() does not cover.


# isidentifier()
# The isidentifier() method in Python is used to check whether a given string is a valid identifier or not. An identifier in Python refers to a name used to identify a variable, function, class, module, or other objects.

#.split() and .strip()
# .split(): Splits a string into a list of substrings based on a specified separator (default is any whitespace), ignoring extra spaces .split() or .split(",").
# .strip(): Removes leading and trailing whitespace (or specified characters) from a string

# Python Lists
# A list is a collection of items (elements) that are ordered and mutable (i.e., you can change the items in the list). Lists are created by placing the items inside square brackets [], separated by commas.
L1 = ["John", 102, "USA"]
L2 = [1, 2, 3, 4, 5, 6]
print(type(L1))  # Output: <class 'list'>
print(type(L2))  # Output: <class 'list'>

# Key Points:
# Ordered: Lists maintain the order of elements.
# Mutable: Items in a list can be changed.
# Flexible: Lists can store elements of different types.

#Common List Methods
# append(x) Method
# Description: Appends an item x to the end of the list.
# Use Case: Useful when you want to add a single item to a list without modifying any of the existing elements.
cubes = [1, 8, 27, 65, 125]
cubes.append(216)  # Adds 216 to the end of the list
print(cubes)  # Output: [1, 8, 27, 65, 125, 216]


# clear() Method
# Description: Removes all items from the list, resulting in an empty list.
# Use Case: When you need to reset a list and remove all its elements.
lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst)  # Output: []

# copy() Method
# Description: Returns a shallow copy of the list.
# Use Case: When you need a copy of a list that is independent of the original list.
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)  # Output: [1, 2, 3]
print(copied_list)    # Output: [1, 2, 3, 4]

# count(x) Method
# Description: Returns the number of times the item x appears in the list.
# Use Case: Useful for counting occurrences of an element in a list.
lst = [1, 2, 2, 3, 2, 4]
print(lst.count(2))  # Output: 3





















