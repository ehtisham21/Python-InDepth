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


# extend(iterable) Method
# Description: Extends the list by appending all the items from the iterable (e.g., another list, tuple).
# Use Case: To combine multiple lists or add elements from an iterable to the current list.

# Original list
my_list = [1, 2, 3]
# List to be added
other_list = [4, 5, 6]
# Extending the original list with other_list
my_list.extend(other_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3]
my_tuple = (4, 5)
# Extend list with a tuple
my_list.extend(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4, 5]


my_list = [1, 2]
my_set = {3, 4}
# Extend list with a set
my_list.extend(my_set)
print(my_list)  # Output: [1, 2, 3, 4]  (order of elements in a set is not guaranteed)



# If we use extend() with a string, each character of the string is added as a separate element as it. When you use the extend() method with a string, each character in the string is treated as a separate item because strings in Python are iterables. This means that Python iterates through the string and adds each individual character to the list, rather than adding the entire string as a single element because extend() is an iterbale method
my_list = [1, 2]
my_string = "abc"
# Extending list with a string
my_list.extend(my_string)
print(my_list)  # Output: [1, 2, 'a', 'b', 'c']


# index(x, start=0, end=len(list)) Method
# Description: Returns the index of the first occurrence of item x. Optional start and end arguments define a range to search within the list.
# Use Case: To find the position of an item in the list.
lst = [1, 2, 3, 4, 2]
print(lst.index(2))  # Output: 1
print(lst.index(2, 2))  # Output: 4 (search starts at index 2)


# insert(i, x) Method
# Description: Inserts item x at index i. Shifts the element currently at that position (if any) and subsequent elements to the right.
# Use Case: To insert an item at a specific position in the list.
lst = [1, 2, 4, 5]
lst.insert(2, 3)  # Insert 3 at index 2
print(lst)  # Output: [1, 2, 3, 4, 5]

# pop(i=-1) Method
# Description: Removes and returns the item at index i. If i is not specified, pop() removes and returns the last item in the list.
# Use Case: Useful for both removing an item from a specific position and for stack-like behavior (LIFO).

lst = [1, 2, 3, 4]
print(lst.pop())  # Output: 4 (removes and returns the last item)
print(lst.pop(0))  # Output: 1 (removes and returns the first item)
print(lst.pop(-1))  # Output: 4 (removes and returns the last index item)

# remove(x) Method
# Description: Removes the first occurrence of item x from the list. Raises a ValueError if the item is not found.
# Use Case: To remove a specific item from a list.
lst = [1, 2, 3, 2, 4]
lst.remove(2)
print(lst)  # Output: [1, 3, 2, 4] (first 2 is removed)

# reverse() Method
# Description: Reverses the elements of the list in place.
# Use Case: To reverse the order of elements in a list.
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)  # Output: [5, 4, 3, 2, 1]


# sort(key=None, reverse=False) Method
# Description: The sort() method in Python is used to sort the elements of a list in place (i.e., it modifies the list directly). It has two optional parameters: key and reverse
# Use Case: To sort elements in a list either in ascending or descending order.
# key: A function that takes one input (an element from the list) and returns a value that will be used to sort the elements. This allows you to sort the list based on custom criteria.
# reverse: A boolean value (default is False). If True, the list will be sorted in descending order; if False (default), the list will be sorted in ascending order.

numbers = [5, 2, 9, 1, 5, 6]
# Sort the list in ascending order (default behavior)
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

numbers = [5, 2, 9, 1, 5, 6]
# Sort the list in descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]

words = ["banana", "apple", "cherry", "date"]
# Sort the list based on the length of each word
words.sort(key=len)
print(words)  # Output: ['date', 'apple', 'banana', 'cherry']


# List Indexing and Slicing
# Lists support indexing and slicing, which allows you to access specific elements or a range of elements.
squares = [1, 4, 9, 16, 25]
print(squares[0])  # Output: 1
print(squares[-1])  # Output: 25
print(squares[-3:])  # Output: [9, 16, 25]
+---+---+---+---+---+
| 1 | 4 | 9 | 16 | 25 |
+---+---+---+---+---+
  0    1   2   3    4
 -5   -4  -3  -2   -1


# Concatenation and Modification
# Lists can be concatenated using the + operator, and you can modify elements by assigning new values.
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]  # Concatenation
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64  # Correcting an incorrect value
print(cubes)  # Output: [1, 8, 27, 64, 125]

# Nested Lists
# Lists can contain other lists, allowing for complex data structures.
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # Output: [['a', 'b', 'c'], [1, 2, 3]]
print(x[0][1])  # Output: 'b'
print(x[1][2])  # Output: 3

# Modifying List Values
# Lists are mutable, meaning their values can be updated using slice assignments.
lst = [1, 2, 3, 4, 5, 6]
lst[2] = 10  # Update the value at index 2
print(lst)  # Output: [1, 2, 10, 4, 5, 6]

c # Update a slice of the list from 1 to 3 index
print(lst)  # Output: [1, 89, 78, 4, 5, 6]

lst[-1] = 25  # Update the last element
print(lst)  # Output: [1, 89, 78, 4, 5, 25]


# Python List Operations
# The concatenation + and repetition * operators work with lists just as they do with strings.
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(l1 * 2 + l2)  # Output: [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8]
print(len(l1))  # Output: 4


#List Comprehension
# List comprehension is a concise way to create or modify lists in Python. It allows you to construct lists using a compact syntax that consists of an expression followed by a for loop, optionally including if conditions.
[expression for item in iterable if condition]
# expression: The operation or value you want to include in the new list.
# item: Each item in the original iterable.
# iterable: The original iterable (like a list, tuple, etc.).
# condition: (Optional) A condition that filters items from the original iterable.


# Creating a List of Tuples
pairs = [(i, j) for i in range(3) for j in range(3)]
print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]



# Slicing Sequences
# Slicing is a technique in Python that allows you to extract parts of a sequence (like lists, strings) using a range of indices. Slicing provides a powerful way to access specific parts of a sequence without modifying the original sequence.
l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # This gives [10, 20]
print(l[2:])  # This gives [30, 40, 50, 60]

# Explanation:
# l[:2]: This slices the list from the start to the second element (excluding index 2). The output is [10, 20].
# l[2:]: This slices the list from the third element (index 2) to the end. The output is [30, 40, 50, 60].


# String Slicing Examples
s = 'bicycle'
print(s[::3])   # 'bye'
print(s[::-1])  # 'elcycib'
print(s[::-2])  # 'eccb'

# Explanation:
# s[::3]: This slices the string with a step of 3, meaning it takes every third character. The output is 'bye'.
# s[::-1]: This slices the string in reverse order, reversing the string. The output is 'elcycib'.
# s[::-2]: This slices the string in reverse order but skips every second character. The output is 'eccb'.

# The start index is included (the slice starts from this index).
# **The end index is excluded (the slice goes up to, but does not include, this index).


#Tuple
# A tuple in Python is an ordered collection of elements and it is immutable. Tuples are defined by enclosing the elements in parentheses () and separating them with commas. Unlike lists, which are mutable, tuples cannot be modified after they are created.
# Use Cases of Tuples
# Immutable Data: Data that should not be changed once assigned.
# Multiple Return Values: Functions can return multiple values in a single tuple.
# Dictionary Keys: Tuples can be used as keys in dictionaries due to their immutability.
# Efficient Data Handling: Tuples have a smaller memory footprint compared to lists.


# Basics - Tuple Packing and Unpacking
# Tuple Packing: When we pack values into a tuple.
# Tuple Unpacking: When we extract values back into variables.

# Tuple Packing
t = 12345, 54321, 'hello!'
print(t)  # Output: (12345, 54321, 'hello!')

# Tuple Unpacking
a, b, c = t
print(a, b, c)  # Output: 12345 54321 hello!



# Creating Tuples
# Empty Tuple:
empty_tuple = ()
print(type(empty_tuple))  # Output: <class 'tuple'>

# Single Element Tuple:
single_tuple = ("Python",)  # Note the comma
print(type(single_tuple))  # Output: <class 'tuple'>

# Multiple Elements:
multi_tuple = (1, 2, 3, "Python", True)
print(multi_tuple)  # Output: (1, 2, 3, 'Python', True)


# Looping Through Tuples
# You can loop through all the values in a tuple using a for loop:
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
# Output:
# 200
# 50

# Modifying Tuples
dimensions = (200, 50)
dimensions[0] = 250  # Raises TypeError: 'tuple' object does not support item assignment because the tuples are immutable.

# Tuple Indexing and Slicing
# Tuples support indexing and slicing, just like lists:
tuple1 = (1, 2, 3, 4, 5, 6)

# Indexing
print(tuple1[0])  # Output: 1
print(tuple1[-1])  # Output: 6

# Slicing
print(tuple1[1:4])  # Output: (2, 3, 4)
print(tuple1[::2])  # Output: (1, 3, 5)


# Deleting Tuples
# While you cannot delete an element from a tuple, you can delete an entire tuple using the del keyword:
tuple1 = (1, 2, 3, 4, 5)
del tuple1
# print(tuple1)  # Raises NameError: name 'tuple1' is not defined


# Example: Using Tuple Methods
# count()	Returns the number of times a specified value appears in the tuple.
# index()	Returns the index of the first occurrence of a specified value in the tuple.
tup = (1, 2, 2, 3, 4, 4, 4, 5)

# count()
print(tup.count(4))  # Output: 3

# index()
print(tup.index(2))  # Output: 1

#Set
# A set is an unordered collection of unique and mutable elements in Python. It is defined by placing elements within curly braces {} or by using the built-in set() function.
# Key Characteristics of a Set:
# Unordered: The elements do not have a defined order.
# Unique: No duplicate elements are allowed.
# Mutable: You can add or remove elements from a set.

# Example 1: Creating a Set Using Curly Braces
# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Example 2: Creating a Set Using the set() Constructor
# Creating a set from a list using the set() constructor
my_set = set([1, 2, 3, 3, 4, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Example 3: Creating an Empty Set
# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()


# Set Methods with Examples
# add(): Adds an element to the set.

# 🍎 Adding an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}
# Explanation: The add() method is used to add a single element to a set. Since sets do not allow duplicates, if the element already exists, it will not be added again.
# clear(): Removes all elements from the set.
# 🧹 Clearing all elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()
# Explanation: The clear() method removes all the elements from the set, resulting in an empty set.

# copy(): Returns a shallow copy of the set.
# 📋 Making a shallow copy of the set
fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.copy()
print(new_fruits)  # Output: {'apple', 'banana', 'cherry'}
# Explanation: The copy() method creates a shallow copy of the set. This means a new set is created, but the elements are references to the same objects in memory.


# What is a Shallow Copy?
# A shallow copy creates a new set object but does not create copies of the elements contained in the original set; instead, it references them. If the elements are immutable (like strings, integers), a shallow copy behaves the same as a deep copy. However, if the set contains mutable objects (like lists or dictionaries), changes to those mutable objects will be reflected in both the original and the copied set.

# difference(): Returns a set containing the difference between two or more sets.
# ➖ Difference between sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)
print(result)  # Output: {1, 2}
# Explanation: The difference() method returns a new set containing elements that are in the first set but not in the second set.


# discard(): Removes the specified item. If the item is not found, it does not raise an error.
# 🚫 Discarding an element
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}
fruits.discard("pear")  # Does nothing since "pear" is not in the set

# intersection(): Returns a set that is the intersection of two or more sets.
# Intersection of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)  # Output: {3, 4}
# Explanation: The intersection() method returns a new set that contains only the common elements from both sets.


# pop(): Removes and returns an arbitrary element from the set.
# 🔄 Popping an element from the set
fruits = {"apple", "banana", "cherry"}
item = fruits.pop()
print(item)  # Output: Random element (e.g., 'banana')
print(fruits)  # Output: Remaining set without the popped element

# remove(): Removes the specified element from the set. If the element is not found, it raises a KeyError.
# 🗑️ Removing an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}
# fruits.remove("pear")  # Raises KeyError

# union(): Returns a set that contains all items from the original set and all items from the specified sets.
# 🔗 Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}
# Explanation: The union() method returns a new set containing all the unique elements from both sets.

# Dictionary
# A dictionary in Python is a collection of unordered key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.
# Key Characteristics of a Dictionary:
# Unordered: The elements are not stored in any particular order.
# Mutable: You can change, add, or remove elements after the dictionary is created.
# Key-value pairs: Each element in the dictionary is a pair, where the key is unique and maps to a specific value.

# A Simple Dictionary Example
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)   #{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)   #{'color': 'green'}


# Using get() to Access Values
# The get() method is useful when you want to access a key's value without risking a KeyError if the key does not exist.
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'No point value assigned.'))   #No point value assigned.


# Looping Through a Dictionary
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

# Looping Through All Keys
# To loop through all keys in a dictionary, use the .keys() method:
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust'}
for name in favorite_languages.keys():
    print(name.title())

# Looping Through All Values
# To loop through all values in a dictionary, use the .values() method:
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# Dictionary Unpacking in Python
# Dictionary unpacking allows you to extract key-value pairs from a dictionary and assign them to variables. This feature makes the code more readable and allows for more concise variable assignments.
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

user_info = {'name': 'Alice', 'age': 30}

# Unpacking the dictionary into the function call
greet_user(**user_info)


# Another Example
def greet_user(**user_info):
    return user_info

user_info = {'name': 'Alice', 'age': 30}
a = greet_user(**user_info)
print(f'Unpacked dictionary: {a}')
# Explanation: The ** operator unpacks the dictionary user_info into keyword arguments for the function greet_user().


# Dictionary Comprehensions
# Dictionary comprehensions provide a concise way to create dictionaries. They are similar to list comprehensions but allow you to generate key-value pairs for dictionaries in a readable, single-line format.
{key_expression: value_expression for item in iterable}

# Example: Creating a Dictionary from a List
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(squares) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#zip() function
# In Python, the zip() function is a built-in function used to combine multiple iterables (e.g., lists, tuples) element by element, creating an iterator of tuples. Each tuple contains elements from the input iterables at the same position. It's commonly used for pairing elements from two or more iterables.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)

# Convert the zip object to a list (or any other collection type)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# List: An ordered, mutable collection that allows duplicates.
# Tuple: An ordered, immutable collection used for fixed sequences of items.
# Set: An unordered, mutable collection that eliminates duplicates.
# Dictionary: An unordered, mutable collection of key-value pairs, where each key is unique.



