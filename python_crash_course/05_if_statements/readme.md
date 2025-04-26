# If Statements in Python
================================

## Table of Contents
-----------------

1. [Simple If Statements](#simple-if-statements)
2. [Checking for Equality](#checking-for-equality)
3. [Checking for Inequality](#checking-for-inequality)
4. [Numerical Comparisons](#numerical-comparisons)
5. [Checking Whether a Value Is in a List](#checking-whether-a-value-is-in-a-list)
6. [If-Else Statements](#if-else-statements)
7. [The if-elif-else Chain](#the-if-elif-else-chain)
8. [Omitting the else Block](#omitting-the-else-block)

## Simple If Statements
----------------------

You can use `if` statements to execute a block of code if a certain condition is met.

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
 if car == 'bmw':
 print(car.upper()) # Output: BMW
 else:
 print(car.title())
# Output:
# Audi
# BMW
# Subaru
# Toyota
```

## Checking for Equality
----------------------

You can use the `==` operator to check if two values are equal.

```python
car = 'bmw'
print(car == 'bmw') # Output: True

car = 'AUDI'
print(car == 'bmw') # Output: False

car = 'BMW'
print(car == 'bmw') # Output: False

car = 'Audi'
print(car.lower() == 'audi') # Output: True
```

## Checking for Inequality
-------------------------

You can use the `!=` operator to check if two values are not equal.

```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!") # Output: Hold the anchovies!
```

## Numerical Comparisons
----------------------

You can use numerical comparisons to check if a value meets a certain condition.

```python
age = 18
print(age == 18) # Output: True

answer = 17
if answer != 42:
 print("That is not the correct answer. Please try again!")
# Output: That is not the correct answer. Please try again!
```

## Checking Whether a Value Is in a List
-----------------------------------------

You can use the `in` operator to check if a value is in a list.

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
 print("YES It's Included") # Output: YES It's Included
else:
 print("Not Included")
```

## If-Else Statements
----------------------

You can use `if-else` statements to execute different blocks of code based on a condition.

```python
age = 17
if age >= 18:
 print("You are old enough to vote!")
 print("Have you registered to vote yet?")
else:
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")
# Output:
# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!
```

## The if-elif-else Chain
---------------------------

You can use `if-elif-else` chains to check multiple conditions.

```python
age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $5.")
else:
 print("Your admission cost is $10.")
# Output: Your admission cost is $5.
```

## Omitting the else Block
---------------------------

You can omit the `else` block if it's not necessary.

```python
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
# Output: Your admission cost is $5.
```