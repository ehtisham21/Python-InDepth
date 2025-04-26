#Tuple
# A tuple looks just like a list except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.

# Key points:
# Ordered (items have a specific position)
# Immutable (cannot be changed after creation)
# Can contain different types (numbers, strings, etc.)
# Since tuples are indexed, lists can have items with the same value


dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping Through All Values in a Tuple Same as Lists
dimensions = (200,50,100,150)
for dimension in dimensions:
    print(dimension)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple can allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple)) #This is a tuple and it's type is string

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #This is not a tuple and it's type is string

