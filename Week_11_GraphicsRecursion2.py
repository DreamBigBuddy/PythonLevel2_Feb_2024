# Snowflake No Recursion
import turtle

def draw_side(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.backward(side_length)
        turtle.right(60)

def draw_snowflake(side_length, depth):
    angle = 360/depth
    for _ in range(depth):
        turtle.forward(side_length)
        turtle.left(60)
        draw_side(side_length/2)
        turtle.left(120)
        turtle.backward(side_length)
        turtle.right(angle)

# Set up the turtle
turtle.speed(0)  # Set the speed to maximum

# Draw the snwoflake
draw_snowflake(100, 15)

# Keep the window
turtle.done()

# Snowflake with Recursion
def draw_snowflake(length, depth):
    if depth <= 0:
        turtle.forward(length)

    for _ in range(6):
        draw_snowflake(length / 3, depth - 1)
        turtle.backward(length / 3)
        turtle.left(60)

draw_snowflake(200, 2)
