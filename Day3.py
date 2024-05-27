# Make a list

my_list =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
newlist_user = []
# write a program that prints out all the elements of the list that are less than 5.
for element in my_list:
    print(element)


# Instead of printing the elements one by one, 
# make a new list that has all the elements less than 5 from this list in it and print out this new list.

for element in my_list:  # This code is producing results for each iteration instead of one final result
    if element > 5:
        new_list.append(element)
        
print(new_list) # Taking this out of the code block solved the iteration issue, i was asking the system to always print the new list

# Write this in one line of Python.
print([ element for element in my_list if element > 5]) # Here is a solution


# Ask the user for a number  

user_number = int(input("Kindly input a number of your choice: "))

# return a list that contains only elements from the original list a that are smaller than that number given by the user.

for element in my_list:
    if element > user_number:
        newlist_user.append(element)

print(newlist_user)

