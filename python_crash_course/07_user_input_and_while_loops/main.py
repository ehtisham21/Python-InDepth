#UserInput
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Using int() to Accept Numerical Input
age = int(input("How old are you? "))
print(age)

#The Modulo Operator
# Modulo operator (%), divides one number by another number and returns the remainder
print(4 % 3)
print(6 % 3)
print(5 % 3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# While Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Using Break keyword in loop
while True:
    city = input("Enter your city")
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


#Using Continue keyword in loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
        print(current_number)


#Using a while Loop with Lists and Dictionaries
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#With Dictionaries
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")