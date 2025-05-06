# 📘 Python File Handling & Exceptions – Beginner Guide

This guide covers the basics of **reading/writing files** and **handling exceptions** in Python. Great for beginners who want to understand file I/O and error handling.

---

## 📂 Reading from a File

### ✅ Reading an Entire File

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

- Opens the file `pi_digits.txt`
- Reads the whole content at once and prints it
- `with` ensures the file is closed automatically

---

### ✅ Reading Line by Line

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
```

- Reads and prints each line one by one
- Useful for large files

---

## ✍️ Writing to a File

### ✅ Writing a Single Line

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

- `'w'` mode **creates or overwrites** the file
- Writes a single line to the file

---

### ✅ Writing Multiple Lines

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```

- Consecutive `.write()` calls to write multiple lines (no newlines unless added)

---

### ➕ Appending to a File

```python
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

- `'a'` mode appends new content without deleting existing content

---

## 📖 File Modes Summary

| Mode | Description                        |
|------|------------------------------------|
| `'r'` | Read (default)                     |
| `'w'` | Write (overwrite if file exists)   |
| `'a'` | Append                             |
| `'r+'`| Read and write                     |

---

## ⚠️ Exceptions in Python

### ❌ Handling ZeroDivisionError

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- Catches the division-by-zero error and prints a message

---

### 🧾 Using the else Block

```python
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)
```

- `else` runs only if the `try` block runs successfully

---

### 🗃 Handling FileNotFoundError

```python
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
```

- Catches the error if a file doesn't exist

---

### 🔁 Using `finally` Block

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Success! You entered: {number}")
finally:
    print("This runs no matter what.")
```

- `finally` always runs, whether there's an error or not
- Commonly used to clean up resources (close files, database, etc.)

---

## 🔄 Summary of Try-Except Structure

```python
try:
    # Code that might fail
except:
    # Code that runs if there’s an error
else:
    # Code that runs if no error
finally:
    # Code that always runs
```

- ✅ `try`: Write risky code here
- 🚫 `except`: Handle specific or general errors
- ➕ `else`: Runs only if try is successful
- 🔚 `finally`: Always runs – good for cleanup

---

Happy Coding! 🚀
