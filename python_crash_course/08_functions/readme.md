**Functions in Python**
========================

Table of Contents
-----------------

1. [Defining a Function](#defining-a-function)
2. [Passing Information to a Function](#passing-information-to-a-function)
3. [Arguments and Parameters](#arguments-and-parameters)
4. [Passing Arguments](#passing-arguments)
    * [Positional Arguments](#positional-arguments)
    * [Keyword Arguments](#keyword-arguments)
5. [Default Values](#default-values)
6. [Return Values](#return-values)
7. [Making an Argument Optional](#making-an-argument-optional)
8. [Returning a Dictionary](#returning-a-dictionary)
9. [Passing a List](#passing-a-list)
10. [Passing an Arbitrary Number of Arguments](#passing-an-arbitrary-number-of-arguments)
11. [Mixing Positional and Arbitrary Arguments](#mixing-positional-and-arbitrary-arguments)

### Defining a Function

A function is a block of code that can be called multiple times from different parts of your program.

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

Output:
```
Hello!
```

### Passing Information to a Function

You can pass information to a function by including arguments in the function definition.

```python
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
```

Output:
```
Hello, Jesse!
```

### Arguments and Parameters

*   Parameters are the variables defined in the function definition.
*   Arguments are the values passed to the function when it's called.

```python
def greet_user(username):  # username is parameter
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')  # jesse is argument
```

### Passing Arguments

There are two types of arguments:

#### Positional Arguments

Positional arguments need to be in the same order as the parameters were written.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
```

Output:
```
I have a hamster.
My hamster's name is Harry.
```

#### Keyword Arguments

Keyword arguments consist of a variable name and a value.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
```

Output:
```
I have a hamster.
My hamster's name is Harry.
```

### Default Values

You can assign default values to parameters.

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
```

Output:
```
I have a dog.
My dog's name is Willie.
```

### Return Values

Functions can return values.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

Output:
```
Jimi Hendrix
```

### Making an Argument Optional

You can make an argument optional by assigning a default value.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

Output:
```
Jimi Hendrix
John Lee Hooker
```

### Returning a Dictionary

Functions can return dictionaries.

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

Output:
```python
{'first': 'jimi', 'last': 'hendrix'}
```

### Passing a List

You can pass lists to functions.

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

Output:
```
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

### Passing an Arbitrary Number of Arguments

You can use `*` to pass an arbitrary number of arguments.

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

Output:
```
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### Mixing Positional and Arbitrary Arguments

You can mix positional and arbitrary arguments.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Output:
```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

You can use `**` to pass an arbitrary number of keyword arguments.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
```

Output:
```python
{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
```