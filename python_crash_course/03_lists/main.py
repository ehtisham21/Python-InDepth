#A list is a collection of items (elements) that are ordered and mutable
# (i.e., you can change the items in the list). Lists are created by placing the items inside square brackets [], separated by commas.


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


#Accessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

#We can also use the string methods from Chapter 2 on any element in
#a list. For example, you can format the element 'trek' more neatly by using the title() method:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

#Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

#Using Individual Values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)


#Adding Elements to a List
#Appending Elements to the End of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)



#Inserting Elements into a List
#You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  #inster takes 2 arguments one is index and the second is value which we want to insert
print(motorcycles)

#Removing Elements from a List
#Removing an Item Using the del Statement
#If you know the position of the item you want to remove from a list, we can use the del statement.
#After using del statement we can no longer access the value that was removed from the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)



#Removing an Item Using the pop() Method
#And after using pop statement we can access the value that was removed from the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#NOTE: If you’re unsure whether to use the del statement or the pop() method,
#here’s a simple way to decide: when you want to delete an item from a list
#and not use that item in any way, use the del statement; if you want to use an
#item as you remove it, use the pop() method.


#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#Note: The remove() method deletes only the first occurrence of the value you specify. If there’s
#a possibility the value appears more than once in the list, you’ll need to use a loop to
#determine if all occurrences of the value have been removed.

#Organizing a List
#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#The sort() method, changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order

#You can also sort this list in reverse alphabetical order by passing the
#argument reverse=True to the sort() method. The following example sorts
#the list of cars in reverse alphabetical order:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)


#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


#Avoiding Index Errors When Working with Lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])  #It will give error as there is no value on 3 index



