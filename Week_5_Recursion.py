# Infinite Shapes
import turtle, random

t = turtle.Turtle()

while True:
    sides = random.randint(3, 10)

    t.penup()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y)
    t.pendown()

    for i in range(sides):
        t.forward(100)
        t.left(((sides-2)*180)/sides)

# Recursion Countdown Example
def countdown(num):
    print(num)

    if num == 0:
        return

    return countdown(num-1)

countdown(5)
