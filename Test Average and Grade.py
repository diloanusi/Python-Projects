#Test Average and Grade

#asks the user to enter five test scores
#display a letter grade for each score and the average test scores

def main():
             #get the test scores
             testScore1 = float(input("Enter test 1: "))
             testScore2 = float(input("Enter test 2: "))
             testScore3 = float(input("Enter test 3: "))
             testScore4 = float(input("Enter test 4: "))
             testScore5 = float(input("Enter test 5: "))

             #get the average of test scores
             average = calc_average(testScore1, testScore2, testScore3, testScore4, testScore5)

             #get the letter grade for each score and the average scores
             letterGrade = determine_grade(average)

             #display score and letter grade 
             print("You scored: \n",
                   "Test 1 grade: ", testScore1, ": ", determine_grade(testScore1), "\n",
                   "Test 2 grade: ", testScore2, ": ", determine_grade(testScore2), "\n",
                   "Test 3 grade: ", testScore3, ": ", determine_grade(testScore3), "\n",
                   "Test 4 grade: ", testScore4, ": ", determine_grade(testScore4), "\n",
                   "Test 5 grade: ", testScore5, ": ", determine_grade(testScore5), "\n",
                   "Average grade: ", average, ": ", determine_grade(average), "\n")
      

#calc_average function accepts 5 test scores as argument
#returns the average of the scores 
def calc_average(t1, t2, t3, t4, t5):
             testAverage = float((t1+t2+t3+t4+t5)/5)
             return testAverage

#determine_grade function accepts a test score as an argument
#returns a letter grade based on (90 - 100) A, (80 -89) B, (70 -79) C, (60, 69) D, (below 60) F
def determine_grade(average):
             grade = " "
             if (average >= 90):
                   grade = "A"
             elif (average >= 80):
                   grade = "B"
             elif (average >= 70):
                   grade = "C"
             elif (average >= 60):
                   grade = "D"
             else: 
                   grade = "F"
             return grade

#call the main function
main()
                                
