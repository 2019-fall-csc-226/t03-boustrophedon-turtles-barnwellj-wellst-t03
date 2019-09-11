#################################################################################
# Author: Jacob Barnwell Taran Wells
# Username: barnwellj wellst
#
# Assignment: TO3
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_square(jimmy):
    """Creates the box for the drawing
    """
    jimmy.penup()
    jimmy.setpos(-250,250)
    jimmy.pendown()

    for s in range(4):
        jimmy.forward(594)
        jimmy.right(90)
        pass
        # ...


def right_turns(jimmy):
    """right turns within the box
    """
    jimmy.forward(550)
    jimmy.right(90)
    jimmy.forward(22)
    jimmy.right(90)
    pass
    # ...
def left_turns(jimmy):
    """left turns within the box
    """
    jimmy.forward(550)
    jimmy.left(90)
    jimmy.forward(22)
    jimmy.left(90)
    pass

def main():
    """
    Docstring for main
    """
    # ...
    wn = turtle.Screen()
    jimmy = turtle.Turtle()
    jimmy.color("black")  # importing the Turtle and screen, applying attributes
    jimmy.pensize(22)
    jimmy.speed(15)

    draw_square(jimmy)            # Function to draw the main square
    jimmy.penup()
    jimmy.forward(22)
    jimmy.right(90)
    jimmy.forward(22)
    jimmy.left(90)
    jimmy.color("blue")
    jimmy.pendown()

    for i in range(12):
      right_turns(jimmy)            # Function call to function_2
      left_turns(jimmy)            # Function call to function_3

    right_turns(jimmy)              #finishes the fill
    jimmy.forward(550)

    wn.exitonclick()

main()

