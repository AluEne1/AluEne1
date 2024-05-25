# Create a program that asks the user to enter their name and their age. 


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("How old did/do you turn this year? ")) # allows the code recognise its working with an integer not a string

# Print out a message addressed to them that tells them the year that they will turn 100 years old. 

import datetime 

curr_year = datetime.date.today().year # To get current year
born_year = curr_year - age 
hund_years = 100 + born_year

print ("Your name is " + first_name + " " + last_name + " and you are " + str(age) + " years old.")
print("You were born in " + str(born_year) + " and you would turn a 100 years in " + str(hund_years) )