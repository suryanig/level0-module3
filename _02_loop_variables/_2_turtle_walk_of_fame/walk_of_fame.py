import turtle

if __name__ == '__main__':
    mrgreen = turtle.Turtle()
    mrgreen.shape('turtle')
    mrgreen.color('blue', 'green')
    mrgreen.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    mrgreen.penup()
    mrgreen.goto(-350,0)
    mrgreen.pendown()
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    for i in range (10):
        for x in range (5):
            mrgreen.forward(30)
            mrgreen.right(144)
        mrgreen.penup()
        mrgreen.goto(-350+i*50, 0)
        mrgreen.pendown()
    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
