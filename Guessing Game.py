#Random Number Guessing Game

#generates a random number in the range of 1 to 100
#ask user to guess what number it is
#if users guess is higher  than random number, display "Too high, try again"
#if users guess is lower  than random number, display "Too low, try again"
#if user guesses the number, congratulate and generate a new random number 

#optional: calculate how many times they guess 

#call random function
import random

def main():
             #get a random number between (1 - 100)
             number = random.randint(1, 100)
             
             #show the number, for this test
             print(number)

             #get the user's guess
             guess = get_guess()

             #display "Too high" message
             high = display_high(guess)

             #display "Too low" message
             low = display_low(guess)

             #congratulate the user
             congrats = congratulation(guess)

             #calculate number of times user guesses answer
             count = 0
             
             #if user enters the wrong answer go through this steps
             while(guess != number):
                          #if guess is higher than number print "too high" text
                          if(guess > number):
                                       print (high)
                          #if lower print "too low" text
                          else:
                                       print(low)

                          #add if they guess wrong and print
                          count += 1
                          print("You've guessed:", count, "times")
                          
                          #ask user to try again, so to get the right number 
                          guess = get_guess()

             total_count1 = count + 1
             #total amount of time guessed
             print("Total Guess:", total_count1)

             #if they guess right, move on to the next step
             if(guess == number):
                          #they guessed right, congratulate them 
                          print(congrats)
                          
                          #prompts user if they want to play again
                          ans = input("Do you want to play again? Y or N: ")
                          while (ans.upper() == 'Y'):
                                       #get a random number between (1 - 100)
                                       number = random.randint(1, 100)

                                       #show number for test
                                       print(number)

                                       #get user's guess
                                       guess = get_guess()
                                       
                                       #count guesses
 #                                      count2 = -1
                                       
                                       while(guess != number):
                                                    #if guess is higher than number print "too high" text
                                                    if(guess > number):
                                                                 print (high)
                                                    #if lower print "too low" text
                                                    else:
                                                                 print(low)

                                                    #add if they guess wrong and print
 #                                                   count2 += 1
                                                    print("You've guessed: ", count, "times")

                                                    #ask user to try again, so to get the right number 
                                                    guess = get_guess()

                                       print(congrats)

                                       #prompt user if they want to play again
                                       ans = input("Do you want to play again? Y or N: ")

##                          total_count2 = count2 + 2
##                          #number of guesses and goodbye message
##                          total = total_count1 + total_count2
#                          print("Total Guesses:", total)
                          print("Thank you for playing")
                          print("Have a good day!")
                          


#get_guess functions gets the user's guess
#returns the value
def get_guess():
             #get the guessed number
             guess_number = int(input("Guess a number: "))
             return guess_number 


#display_high function accepts the guessed number as an argument
#returns the message "Too high, try again"
def display_high(guess):
             message ="Too high, try again"
                          
             #return the too high text              
             return message 


#display_high function accepts the guessed number as an argument
#returns the message "Too high, try again"
def display_low(guess):
             message = "Too low, try again"

             #return the too low text              
             return message 


#congratulation function accepts the guessed number as an argument
#returns the message "Congratulation"
def congratulation(guess):
             message = "Congratulations!, you're correct"

             #return the congratulation text              
             return message 

                                
#call main function
main()
