# Do Not Enter Sign
import turtle

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(0, -100)
t.pendown()

t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()

t.color("white")
t.penup()
t.goto(-80, 10)
t.pendown()

t.begin_fill()
for i in range(2):
    t.forward(160)
    t.right(90)
    t.forward(20)
    t.right(90)

t.end_fill()

t.penup()
t.goto(-62, 18)
t.pendown()

t.write("Do Not", font=('Arial', 30, 'bold'))

t.penup()
t.goto(-50, -65)
t.pendown()

t.write("Enter", font=('Arial', 30, 'bold'))

t.hideturtle()

# Yield Sign
import turtle

t = turtle.Turtle()
t.speed(0)

t.color("red")
t.begin_fill()
for i in range(3):
    t.forward(300)
    t.right(120)

t.end_fill()

t.color("white")

t.penup()
t.goto(60, -40)
t.pendown()

t.begin_fill()
for i in range(3):
    t.forward(200)
    t.right(120)

t.end_fill()

t.penup()
t.goto(80, -100)
t.pendown()

t.color("red")
t.write("Yield", font=("Arial", 50, "bold"))
