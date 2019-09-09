#################################################################################
# Author:
# Username:
#
# Assignment:
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
wn = turtle.Screen()
jimmy = turtle.Turtle()
jimmy.color("black")
jimmy.pensize(22)







def function_1():
    """Creates the box for the drawing
    """
jimmy.penup()
jimmy.setpos(-250,250)
jimmy.pendown()

for s in range(4):
    jimmy.forward(500)
    jimmy.right(90)


    pass
    # ...


def function_2():
    """
    Docstring for function_2
    """
    pass
    # ...


def main():
    """
    Docstring for main
    """
    # ...
    function_1()            # Function call to function_1
    function_2()            # Function call to function_2


main()

wn.exitonclick()