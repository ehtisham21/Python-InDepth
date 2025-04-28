#Defining a Function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()


#Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')


#Arguments and Parameters
def greet_user(username):  #username is parameter
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse') #jesse is argument


#Passing Arguments
#Types of arguments 1) Positional Arguments 2)Keyword Arguments

#Positional Arguments
#Positional arguments, needs to be in functions the same order the parameters were written
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')



#Keyword Arguments
#Keyword arguments, where each argument consists of a variable name and a value.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')


#Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')



#Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an Argument Optional ( To add optional argument just use default values to make an argument optional.)

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


#Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Passing an Arbitrary Number of Arguments
#Arbitrary Arguments is used when we don't know how many argument we will get while function call.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
         print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#In Arbitrary Number of Arguments we use single * when we don't know how many argument will be passed.
#We use double * (**) when we don't know how many arguments will be passed but we also don't know what type of information will be passed
#So we use ** to get the key, value as an argument.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

