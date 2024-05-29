# write a program that returns a list that contains only the elements that are common between the lists (without duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for x in a: # For each data in list a
    for y in b: # Check each data in list b
        if x == y: # If they are same
            c.append(x) # Put into list c
            
c = list(dict.fromkeys(c)) # Remove duplicates in a list
print(c)


# Writing the above code with random numbers with the Set BUILT IN FUCTION

import random

d = random.sample(range(25,175), 34) # create a random sample from 25 - 174 with 34 numbers
e = random.sample(range(150), 63) # create a random sample form 0 - 149 with 63 number
result = [i for i in set(d) if i in e] # for each element in set(D) - sets don't have duplicates, so there would be no duplicate figures -  if it is in e put it in the list
print(d)
print(e)
print(result)
