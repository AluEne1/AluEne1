# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

num = int(input("Kindly input a number of your choice: ")) # get input
num_list = range(1, num) 
div_list = [] # store divisors



for elem in num_list:
    if num % elem == 0:
        div_list.append(elem)

print(div_list)
