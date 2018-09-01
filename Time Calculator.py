#Time Calculator
#asks user to enter a number of seconds
#if greater than or equal to 60, convert input to minutes and seconds
#if greater than or equal to 3600, convert input to hours, minutes, seconds
#if greater than or equal to 86400, convert input to days, hours, minutes, seconds

#set seconds to 0
seconds = 0

#set minutes = 0
minutes = 0

#set hours = 0
hours = 0

#set days = 0
days = 0

#welcome message
print("Welcome to The Time Calculator")

#ask user to enter number of seconds
numberOfSeconds = int(input("Enter Seconds: "))

#if number of seconds < 60, print what the user entered as seconds  
if(numberOfSeconds < 60):
             seconds = numberOfSeconds
             print("The Time is", seconds, "seconds.")
#if input < 3600, then convert to minutes and seconds 
elif(numberOfSeconds < 3600):
             minutes = int(numberOfSeconds/60)
             seconds = int(numberOfSeconds%60)
             print("The Time is", minutes, "Minute(s)", seconds, "Second(s)")
#if input < 86400, convert to hours, minutes and seconds
elif(numberOfSeconds < 86400):
             hours = int(numberOfSeconds/3600)
             minutes = int((numberOfSeconds%3600)/60)
             seconds = int((numberOfSeconds%3600)%60)
             print("The Time is", hours, "Hour(s)", minutes, "Minute(s)", seconds, "Second(s)")
#if input doesn't fit any of the above criteria, do this.
else:
             days = int(numberOfSeconds/86400)
             hours = int((numberOfSeconds%86400)/3600)
             minutes = int(((numberOfSeconds%86400)%3600)/60)
             seconds = int(((numberOfSeconds%86400)%3600)%60)
             print("The Time is", days, "Day(s)", hours, "Hour(s)", minutes, "Minute(s)", seconds, "Second(s)")
             
             
             
             
