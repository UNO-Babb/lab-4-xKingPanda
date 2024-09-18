#TurtleGraphics.py
#Name:Michael Fuller
#Date:9/18/2024
#Assignment:Lab 4

import turtle  # needed generally but not in CodeHS
hideturtle()  # hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides, size):
    angle = 360 / sides
    for _ in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)

def fillCorner(myTurtle, size, corner):
    # Draw the main square
    drawSquare(myTurtle, size)
    
    offset = size / 2

    # Move to the corner
    myTurtle.penup()
    if corner == 1:  # Top-left
        myTurtle.goto(0, 0)
        
    elif corner == 2:  # Top-right
        myTurtle.goto(offset, 0)
        
    elif corner == 3:  # Bottom-left
        myTurtle.goto(0, 0 - offset)
        
    elif corner == 4:  # Bottom-right
        myTurtle.goto(offset, 0 - offset)
        
    myTurtle.pendown()

    # Draw and fill the smaller square in the corner
    myTurtle.begin_fill()
    drawSquare(myTurtle, offset)
    myTurtle.end_fill()

def squaresInSquares(myTurtle, size, num):
    shrink = size / num  #how much each square will shrink

    for i in range(num):
        drawSquare(myTurtle, size)  # Draw the outer square
        myTurtle.penup()
        myTurtle.goto(myTurtle.xcor() + shrink / 2, myTurtle.ycor() - shrink / 2)  # Recenter the turtle
        myTurtle.pendown()
        size -= shrink  # Reduce the size for the next square

def main():
    myTurtle = turtle.Turtle()
    
    #ENTER TESTS FROM HERE-----------------------------------------
    fillCorner(myTurtle, 200, 3)
    #squaresInSquares(myTurtle, 200, 12)  

main()
