import random
import turtle
from tkinter import messagebox, simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    mrgreen = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)

    #      3) Set the pen width to 10
    mrgreen.width(10)
    #      4) Ask the user what color pen they would like to draw with
    color = simpledialog.askstring(title= 'Color?', prompt= "What color wold you like to draw with?")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested

    for i in range (10):
        if color == "red":
            mrgreen.pencolor('red')
        elif color == "blue":
            mrgreen.pencolor('blue')
        elif color == "black":
            mrgreen.pencolor('black')
        elif color == "yellow":
            mrgreen.pencolor('yellow')
        elif color == "green":
            mrgreen.pencolor('green')
        else:
            mrgreen.pencolor('black')
    for i in range (4):
        mrgreen.forward(90)
        mrgreen.right(90)
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
