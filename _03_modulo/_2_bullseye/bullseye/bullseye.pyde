

def setup():
    # Set the size of your sketch
    size (400,400)
    
    

def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    x = 350
    y = 350
    
    for i in range (8):
        ellipse (200,200,x,y)
        x = x-44
        y = y-44
    
    # Use an if statement and modulo to alternate the color of your rings
        if i % 2 == 0:
            fill (0,0,0)
        else:
            fill (255,0,0)
    
