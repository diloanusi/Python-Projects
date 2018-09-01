#Body Mass Index
#asks user to enter his or her weight and height
#display the user's BMI
#display a message indicating whether the person has optimal weight, underweight or overweight

#welcome message
print("Welcome to Body Mass Index Thingy")

#ask user for height
height = float(input("Enter your height: "))

#asks user for weight
weight = float(input("Enter your weight: "))

#Calculate the BMI
bmi = (weight * 703)/(height ** 2)

#if bmi < 18.5, underweight
if(bmi < 18.5):
             print("Your BMI is:", format(bmi, '.1f'))
             print("You're Underweight")
#if bmi > 25, overweight 
elif(bmi > 25):
             print("Your BMI is:", format(bmi, '.1f'))
             print("You're Overweight")
else:
             print("Your BMI is:", format(bmi, '.1f'))
             print("You're Optimal")
