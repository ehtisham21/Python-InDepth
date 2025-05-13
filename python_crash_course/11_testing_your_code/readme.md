# Testing Functions and Classes in Python

This repository demonstrates how to write and test Python functions and classes using the `unittest` module. It includes examples of function testing, handling errors, and writing test cases for classes.

---

## 1. Function Testing Example

### Code

```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
```

### Sample Output

```
Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
    Neatly formatted name: Janis Joplin.

Please give me a first name: q
```

---

## 2. Unit Testing

### ✅ Passing Test Example

```python
import unittest

def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

---

### ❌ Failing Test Example

This version of the function expects three arguments (first, middle, last), but only two are passed in the test case, causing a `TypeError`.

```python
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

### Error Output

```
TypeError: get_formatted_name() missing 1 required positional argument: 'last'
```

---

## 3. Adding New Tests for Middle Name

```python
def get_formatted_name(first, middle='', last=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

import unittest

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', last='joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'amadeus', 'mozart')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```

---

## 4. Testing a Class

### Class Definition

```python
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
```

---

### Unit Test

```python
import unittest

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

unittest.main()
```

### Output (if test passes)

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

## Notes

- Be careful with indentation inside `if` blocks.
- Always match the number of arguments expected by a function with the number used in tests.
- Use descriptive test names and docstrings to clarify intent.
- Don't forget to call `unittest.main()` only once in your script to avoid conflicts.

---
