# 🐍 Python Basics – Learning Journal

This project is a collection of beginner-level Python examples that demonstrate how Python handles variables, strings, numbers, and basic syntax. It's great for anyone just getting started with Python programming.

---

## 📁 Table of Contents

- [Getting Started](#getting-started)
- [Variables](#variables)
- [Strings](#strings)
- [String Methods](#string-methods)
- [Concatenation](#concatenation)
- [Whitespace and Formatting](#whitespace-and-formatting)
- [Stripping Whitespace](#stripping-whitespace)
- [Avoiding Syntax Errors](#avoiding-syntax-errors)
- [Working with Numbers](#working-with-numbers)
- [Float Arithmetic](#float-arithmetic)
- [Type Conversion](#type-conversion)
- [Comments and Line Continuation](#comments-and-line-continuation)

---

## ✅ Getting Started

Make sure you have Python installed. You can run this script with:

```bash
python filename.py
```

Replace `filename.py` with the actual name of the Python file.

---

## 📝 Variables

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

---

## 🔤 Strings

Python strings can be written using:
```python
"This is a string."    # Double quotes
'This is also a string.' # Single quotes
```

Multiline strings use triple quotes:
```python
text = """This is a long string
that spans multiple lines."""
```

---

## 🧹 String Methods

Useful methods to format strings:

```python
name = "ada lovelace"
print(name.title())   # Ada Lovelace
print(name.upper())   # ADA LOVELACE
print(name.lower())   # ada lovelace
```

---

## ➕ Concatenation

Joining strings together:

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")
```

---

## ⬜ Whitespace and Formatting

You can add tabs and newlines to format your text:

```python
print("\tPython")  # Tab
print("Languages:\nPython\nC\nJavaScript")  # Newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")  # Mixed
```

---

## ✂️ Stripping Whitespace

To remove unnecessary spaces:

```python
favorite_language = ' python '
favorite_language.rstrip()  # Removes space from the right
favorite_language.lstrip()  # From the left
favorite_language.strip()   # From both sides
```

---

## ⚠️ Avoiding Syntax Errors

Correct usage with quotes:
```python
message = "One of Python's strengths is its diverse community."
print(message)
```

Incorrect usage that causes an error:
```python
message = 'One of Python's strengths is its diverse community.'  # ❌
```

Use double quotes if your string contains an apostrophe.

---

## 🔢 Working with Numbers

Basic operations:
```python
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
```

Exponentiation:
```python
print(3 ** 2)  # 9
print(3 ** 3)  # 27
print(10 ** 6)  # 1000000
```

---

## 💧 Float Arithmetic

Floating point math can lead to precision issues:

```python
print(0.2 + 0.1)  # 0.30000000000000004
print(3 * 0.1)    # 0.30000000000000004
```

---

## 🔄 Type Conversion

You can't mix strings and integers directly:

```python
age = 23
# message = "Happy " + age + "rd Birthday!"  # ❌ TypeError

message = "Happy " + str(age) + "rd Birthday!"  # ✅
print(message)
```

---

## 💬 Comments and Line Continuation

Single-line comments start with `#`:

```python
x = 10  # This is a comment
```

Use backslashes to continue a line:

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6
```

---

## 🧠 Summary

This project gives you a strong foundation in:
- Variables and strings
- Formatting and concatenation
- Basic arithmetic and floats
- Handling type errors
- Writing readable and clean Python code

Happy coding! 🚀
