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
