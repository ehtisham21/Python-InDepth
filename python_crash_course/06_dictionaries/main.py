#Dictionaries
# A dictionary in Python is a collection of key-value pairs.
# Each key is unique and is used to access its corresponding value.
# Dictionaries are created by placing key-value pairs inside curly braces {}, with a colon : separating keys and values.

# Key points:
# Unordered and Mutable (you can add, change, or remove key-value pairs after creation)
# Keys must be unique and immutable (like strings, numbers, tuples)
# Values can be of any data type (numbers, strings, lists, other dictionaries, etc.)
# Access values by using their keys, not by index


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#Example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


#Looping Through a Dictionary
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}


for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# values() returns all the values in the dictionary.
# items() returns all key-value pairs as a list of tuples.
print(user_0.values())
print(user_0.items())


#Looping Through All the Keys in a Dictionary
#keys will return only the list of all the keys of the dictionary

for name in user_0.keys():
    print(name.title())
#OR (Both do the same thing)

for name in user_0:
    print(name.title())


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'Alex': 'ruby',
    'phil': 'python'
}

# sorted() tells Python to list all keys in the dictionary and sort that list before looping through it.
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Using Set() around a list that contains duplicate items, Python
#identifies the unique items in the list and builds a set from those items. As
#we use set() to pull out the unique values.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


#Nesting
#A List of Dictionaries

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(5):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens:
    print(alien)
    print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
print(aliens)



#A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")

for language in languages:
    print("\t" + language.title())


#A Dictionary in a Dictionary
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