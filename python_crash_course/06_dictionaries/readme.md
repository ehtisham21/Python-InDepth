# Dictionaries in Python
================================

## Table of Contents
-----------------

1. [Introduction to Dictionaries](#introduction-to-dictionaries)
2. [Key Points About Dictionaries](#key-points-about-dictionaries)
3. [Accessing Values in a Dictionary](#accessing-values-in-a-dictionary)
4. [Adding New Key-Value Pairs](#adding-new-key-value-pairs)
5. [Modifying Values in a Dictionary](#modifying-values-in-a-dictionary)
6. [Removing Key-Value Pairs](#removing-key-value-pairs)
7. [Looping Through a Dictionary](#looping-through-a-dictionary)
8. [Nesting](#nesting)

## Introduction to Dictionaries
-------------------------------

A dictionary in Python is a collection of key-value pairs. Each key is unique and is used to access its corresponding value.

## Key Points About Dictionaries
--------------------------------

* **Unordered and Mutable**: You can add, change, or remove key-value pairs after creation.
* **Keys must be unique and immutable**: Keys can be strings, numbers, or tuples, but not lists or dictionaries.
* **Values can be of any data type**: Values can be numbers, strings, lists, other dictionaries, etc.

## Accessing Values in a Dictionary
----------------------------------

You can access values in a dictionary by their keys.

```python
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color']) # Output: green
print(alien_0['points']) # Output:5
```

## Adding New Key-Value Pairs
---------------------------

You can add new key-value pairs to a dictionary.

```python
alien_0 = {'color': 'green', 'points':5}
print(alien_0)
alien_0['x_position'] =0
alien_0['y_position'] =25
print(alien_0)
# Output:
# {'color': 'green', 'points':5}
# {'color': 'green', 'points':5, 'x_position':0, 'y_position':25}
```

## Modifying Values in a Dictionary
----------------------------------

You can modify values in a dictionary.

```python
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".") # Output: The alien is green.
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".") # Output: The alien is now yellow.
```

## Removing Key-Value Pairs
---------------------------

You can remove key-value pairs from a dictionary.

```python
alien_0 = {'color': 'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0) # Output: {'color': 'green'}
```

## Looping Through a Dictionary
------------------------------

You can loop through a dictionary using the `.items()`, `.values()`, or `.keys()` methods.

```python
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
 print("\nKey: " + key)
 print("Value: " + str(value))
# Output:
# Key: username
# Value: efermi

# Key: first
# Value: enrico

# Key: last
# Value: fermi
```

## Nesting
------------

### A List of Dictionaries

You can store a list of dictionaries.

```python
aliens = []
for alien_number in range(5):
 new_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
 aliens.append(new_alien)

for alien in aliens:
 print(alien)
 print("...")
# Output:
# {'color': 'green', 'points':5, 'speed': 'slow'}
# ...
print("Total number of aliens: " + str(len(aliens))) # Output: Total number of aliens:5
```

### A List in a Dictionary

You can store a list in a dictionary.

```python
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping)
# Output:
# You ordered a thick-crust pizza with the following toppings:
#     mushrooms
#     extra cheese
```

### A Dictionary in a Dictionary

You can store a dictionary in another dictionary.

```python
users = {
'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
},
'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
},
}

for username, user_info in users.items():
 print("\nUsername: " + username)
 full_name = user_info['first'] + " " + user_info['last']
 location = user_info['location']
 print("\tFull name: " + full_name.title())
 print("\tLocation: " + location.title())
# Output:
# Username: aeinstein
#     Full name: Albert Einstein
#     Location: Princeton

# Username: mcurie
#     Full name: Marie Curie
#     Location: Paris
```