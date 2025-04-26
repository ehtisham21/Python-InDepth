#If Statements

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#Checking for Equality
car = 'bmw'
car == 'bmw' #Result will be True

car = 'AUDI'
car == 'bmw' #Result will be False

car = 'BMW'
car == 'bmw' #Result will be False

car = 'Audi'
car.lower() == 'audi' #Result will be True


#Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Numerical Comparisons
age = 18
print(age == 18) #Result will be True

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


#Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if  'mushrooms' in requested_toppings:
    print("YES It's Included")
else:
    print("Not Included")

#If-Else
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#Omitting the else Block
#Python does not require an else block at the end of an if-elif chain. Some
# times an else block is useful; sometimes it is clearer to use an additional
# elif statement that catches the specific condition of interest:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")