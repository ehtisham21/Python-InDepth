# Tuples in Python
================================

## Table of Contents
-----------------

1. [Introduction to Tuples](#introduction-to-tuples)
2. [Key Points About Tuples](#key-points-about-tuples)
3. [Accessing Elements in a Tuple](#accessing-elements-in-a-tuple)
4. [Looping Through All Values in a Tuple](#looping-through-all-values-in-a-tuple)
5. [Creating Tuples](#creating-tuples)
6. [Tuple Length](#tuple-length)
7. [Creating Tuples with One Item](#creating-tuples-with-one-item)

## Introduction to Tuples
------------------------

A tuple is a collection of items that are ordered and immutable. Tuples are defined using parentheses `()` instead of square brackets `[]`.

## Key Points About Tuples
---------------------------

*   **Ordered**: Tuples maintain the order in which items were added.
*   **Immutable**: Tuples cannot be changed after creation.
*   **Can contain different types**: Tuples can contain different data types, such as numbers, strings, etc.
*   **Indexed**: Tuples are indexed, which means you can access individual elements by their index.

## Accessing Elements in a Tuple
--------------------------------

You can access elements in a tuple by their index.

```python
dimensions = (200, 50)
print(dimensions[0]) # Output: 200
print(dimensions[1]) # Output: 50
```

## Looping Through All Values in a Tuple
-----------------------------------------

You can loop through all values in a tuple using a `for` loop.

```python
dimensions = (200, 50, 100, 150)
for dimension in dimensions:
    print(dimension)
# Output:
# 200
# 50
# 100
# 150
```

## Creating Tuples
------------------

You can create tuples using parentheses `()`.

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple) # Output: ('apple', 'banana', 'cherry')
```

## Tuples Allow Duplicates
-------------------------

Tuples can contain duplicate values.

```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')
```

## Tuple Length
----------------

You can find the length of a tuple using the `len()` function.

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # Output: 3
```

## Creating Tuples with One Item
---------------------------------

To create a tuple with one item, you need to include a trailing comma.

```python
thistuple = ("apple",)
print(type(thistuple)) # Output: <class 'tuple'>
```

Without a trailing comma, Python does not treat the variable as a tuple.

```python
thistuple = ("apple")
print(type(thistuple)) # Output: <class 'str'>
```

In this case, `thistuple` is treated as a string, not a tuple.