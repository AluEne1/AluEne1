# Ask the user for a number.    

num = int(input("Kindly input a number of your choice: "))

# Depending on whether the number is even or odd, print out an appropriate message to the user
if num % 2 == 0:
    print("You have inputed an even number!")
else:
    print("You have inputed an odd number!")

if num % 4 == 0:
    print("This number is also multiple of 4")
else:
    print("This number is not a multiple of 4")
# If the number is a multiple of 4, print out a different message.


# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 

num1 = int(input("Kindly input a number of your choice: "))
check = int(input("Kindly input a number of your choice: "))

# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

if num1 % check == 0:
    print(str(num1) + " is divisible by " + str(check))
else:
    print(str(num1) + " is not divisible by " + str(check))