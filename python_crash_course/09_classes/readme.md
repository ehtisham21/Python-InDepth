# 🚗 Python OOP Concepts: Dog & Car Modeling

This Python script demonstrates key Object-Oriented Programming (OOP) concepts such as **classes**, **attributes**, **inheritance**, **method overriding**, and **instances as attributes** using two primary examples: `Dog` and `Car`.

---

## 📘 Table of Contents

- [Dog Class](#dog-class)
- [Car Class](#car-class)
- [Inheritance](#inheritance)
- [Method Overriding](#method-overriding)
- [Instances as Attributes](#instances-as-attributes)
- [Output](#output)
- [Conclusion](#conclusion)

---

## 🐶 Dog Class

The `Dog` class is a simple example that models the behavior of a dog.

### Features:

- Stores dog's name and age
- Includes methods:
  - `sit()`: Simulates the dog sitting
  - `roll_over()`: Simulates the dog rolling over

```python
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
```

---

## 🚗 Car Class

The `Car` class is designed to model a general car.

### Features:

- Attributes: make, model, year, odometer
- Methods:
  - `get_descriptive_name()`: Returns car info
  - `read_odometer()`: Displays mileage
  - `fill_gas_tank()`: Simulates filling the gas tank

```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def fill_gas_tank(self):
        print("This car need a gas tank!")
```

---

## 🧬 Inheritance

The `ElectricCar` class inherits from `Car` to extend its functionality for electric cars.

### Additions:

- Inherits car properties
- Adds `battery_size`
- Method: `describe_battery()`

```python
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

---

## 🔁 Method Overriding

The `ElectricCar` overrides the `fill_gas_tank()` method to reflect that electric cars don't use gas.

```python
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name(), my_tesla.fill_gas_tank())
my_tesla.describe_battery()
```

---

## 🧱 Instances as Attributes

The battery of the electric car is modeled as a separate `Battery` class and used as an instance inside `ElectricCar`.

```python
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

---

## 🖨️ Output

```
My dog's name is Willie.
My dog is 6 years old.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.

2016 Tesla Model S
2016 Tesla Model S
This car has a 70-kWh battery.
2016 Tesla Model S This car doesn't need a gas tank!
This car has a 70-kWh battery.
2016 Tesla Model S
This car has a 70-kWh battery.
```

---

## ✅ Conclusion

This example code covers foundational OOP concepts in Python, including:

- ✅ Class creation
- ✅ Inheritance
- ✅ Method Overriding
- ✅ Composition (instances as attributes)

These are crucial building blocks for building real-world object-oriented applications in Python.
