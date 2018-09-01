#February Days
#asks user to enter a year
#display number of days in February that year

#welcome message
print("Welcome")

#ask user to enter a year
year = int(input("Enter a Year: "))

#its a leap year if divisible by 4, and not divisible by 100
if(year%100 != 0):
             if(year%4 == 0):
                          print("In this year, February will have 29 days.")
             else:
                          print("In this year, February will have 28 days.")
elif(year%100 == 0):
             if(year%400 == 0):
                          print("In this year, February will have 29 days.")
             else:
                          print("In this year, February will have 28 days.")
else:
             print("In this year, February will have 28 days.")
