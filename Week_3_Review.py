import turtle

t = turtle.Turtle()

t.begin_fill()
for i in range(8):
    t.forward(100)
    t.right(45)

t.fillcolor("red")
t.end_fill()

t.penup()
t.goto(-25, -140)
t.pendown()

t.color("white")
t.write("STOP", font=("Arial", 50, "bold"))
