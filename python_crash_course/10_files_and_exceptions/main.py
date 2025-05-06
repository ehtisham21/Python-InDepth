#Reading from a File
#Reading an Entire File
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

#Reading Line by Line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

#Writing to a File
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

#You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
# you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.


#Writing Multiple Lines
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")


#Appending to a File
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")



#Exceptions
#Handling the ZeroDivisionError Exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")



#The else Block
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:  # The else in exception will execute only when try block will be successful nad don't return any error.
    print(answer)


#Handling the FileNotFoundError Exception
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
    contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)


#Using finally in exception
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Success! You entered: {number}")
finally:
    print("This runs no matter what.")

# try: Runs the risky code.
# except: Runs only if an exception happens in try.
# else: Runs only if no exception happened in try.
# finally: Runs always, no matter if there was an error or not. It's often used for cleanup, like closing a file or a database connection.



