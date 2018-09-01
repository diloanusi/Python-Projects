#Shipping Charges
#asks the user to enter the weight of a package
#displays the shipping charges

#rates per pound < 3
RATE1 = 1.50
#rates per pound < 7 
RATE2 = 3.00
#rates per pound < 10
RATE3 = 4.00
#rates per pound for everything else
RATE4 = 4.75

#welcome message
print("Welcome to The Fast Freight Shipping Company")

#get weight of a package
weight = int(input("Enter the weight of package(s): "))

#set shipping charges to 0, no item yet
charges = 0

#if the weight < 3
if(weight < 3):
             #depending on how much product weighs, multiply by rate to get charges
             charges = weight * RATE1
             print("Shipping Charges will be $", format(charges, '.2f'))
#if the weight < 7
elif(weight < 7):
              #depending on how much product weighs, multiply by rate to get charges
             charges = weight * RATE2
             print("Shipping Charges will be $", format(charges, '.2f'))
#if the weight < 10
elif(weight < 10):
              #depending on how much product weighs, multiply by rate to get charges
             charges = weight * RATE3
             print("Shipping Charges will be $", format(charges, '.2f'))
#if the weight is everything else 
else:
              #depending on how much product weighs, multiply by rate to get charges
             charges = weight * RATE4
             print("Shipping Charges will be $", format(charges, '.2f'))
