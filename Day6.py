# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.) 

wrd = input("Kindly input a word of your choice: ") # Get an input
wrd = str(wrd) # Turn input to string
rvs = wrd[:: -1] # slicing will start from the end of the string with one step back each time

if wrd == rvs:
    print(wrd + " is a palindrome!")
else:
    print(wrd + " is not a palindrome")