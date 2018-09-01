#Calculating the factorial of a number
#ask user to enter a nonnegative integer
#use a loop to calculate the factorial of that number
#display the factorial

#welcome message
print("Welcome to Number Factorial")
#ask user for input
user_input = int(input("Enter a positive integer: "))

#set a rule to prevent user from entering a negative number
while user_input < 0:
             user_input = int(input("Please enter a positive integer: "))

#set accumulator for the calculation
total = 1 #not 0, if not outcome will always be 0

#loop from 1 to input by user
for number in range(user_input):
             number += 1
             total *= number
             print(number)
print ("The factorial is", total)
