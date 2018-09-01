#Software Sales
#asks user to enter number of packages purchased
#display amount of the discount (if any) and total amount of the purchase after the discount

#price of packages 
PRICE = 99
#discount for 10 - 19 packages 
DISCOUNT1 = 0.10
#discount for 20 - 49 packages 
DISCOUNT2 = 0.20
#discount for 50 -99 packages 
DISCOUNT3 = 0.30
#discount for 100 or more packages 
DISCOUNT4 = 0.40

#welcome message
print("Welcome to 'A Software Company'")

#Get number of packages purchased
package = int(input("Enter number of package(s) purchased: "))

#set price to zero, no items yet
price = 0

#set total purchase to zero, no purchase yet 
total = 0

#set discount to zero, since its not been used yet
discount = 0

#if the number of package is below 10, then each package will be $99
if(package < 10):
             #depending on the number of packages bought, price is derived
             price = package * PRICE
             #add to the total purchase; therefore initial total (0) = total(0) + price
             total += price
             #print out total amount, and discount
             print("Total Purchase is: $", format(total, '.2f'))
             print("Total Discount: $", format(discount, '.2f'))
#if the number of package is between 10 & 19, then each package will be package * ($99 - ($99 * 0.10)) 
elif(package < 20):
             #discount will be..
             discount = (PRICE - (PRICE * DISCOUNT1)) 
             #depending on the number of packages bought and discount used, price is derived
             price = package * discount
             #add to the total purchase; therefore initial total (0) = total(0) + price
             total += price
             #print out total amount, and discount
             print("Total Purchase is: $", format(total, '.2f'))
             print("Total Discount: $", format(discount, '.2f'))
#if the number of package is between 20 & 49 , then each package will be package * ($99 - ($99 * 0.20)) 
elif(package < 50):
             #discount will be..
             discount = (PRICE - (PRICE * DISCOUNT2)) 
             #depending on the number of packages bought and discount used, price is derived
             price = package * discount
             #add to the total purchase; therefore initial total (0) = total(0) + price
             total += price
             #print out total amount, and discount
             print("Total Purchase is: $", format(total, '.2f'))
             print("Total Discount: $", format(discount, '.2f'))
#if the number of package is between 50 & 99, then each package will be package * ($99 - ($99 * 0.30)) 
elif(package < 100):
             #discount will be..
             discount = (PRICE - (PRICE * DISCOUNT3)) 
             #depending on the number of packages bought and discount used, price is derived
             price = package * discount
             #add to the total purchase; therefore initial total (0) = total(0) + price
             total += price
             #print out total amount, and discount
             print("Total Purchase is: $", format(total, '.2f'))
             print("Total Discount: $", format(discount, '.2f'))
#if the number of package is 100 or more, then each package will be package * ($99 - ($99 * 0.40)) 
else:
             #discount will be..
             discount = (PRICE - (PRICE * DISCOUNT4)) 
             #depending on the number of packages bought and discount used, price is derived
             price = package * discount
             #add to the total purchase; therefore initial total (0) = total(0) + price
             total += price
             #print out total amount, and discount
             print("Total Purchase is: $", format(total, '.2f'))
             print("Total Discount: $", format(discount, '.2f'))
              
