#Turtle Graphics: Repeating Squares

#turtle graphics program that uses nested loops to draw 100 squares
import turtle
NUM_SQUARES = 100 #number of squares to draw
FORWARD = 5 #distance turtle travels

#draw 100 squares, increasing each new one by 2
for x in range(NUM_SQUARES):
             turtle.setheading(90)
             turtle.forward(FORWARD)
             turtle.setheading(180)
             turtle.forward(FORWARD)
             turtle.setheading(270)
             turtle.forward(FORWARD)
             turtle.setheading(360)
             turtle.forward(FORWARD)
             FORWARD *= 2
       
