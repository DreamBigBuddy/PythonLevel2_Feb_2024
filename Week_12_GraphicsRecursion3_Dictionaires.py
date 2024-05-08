# Snowflake No Recursion
import turtle

def draw_side(side_length):
    for _ in range(6):
        turtle.forward(side_length)

        for j in range(6):
            turtle.forward(side_length/3)
            turtle.backward(side_length/3)
            turtle.right(60)
        
        turtle.backward(side_length)
        turtle.right(60)

def draw_snowflake(side_length, depth):
    angle = 360/depth
    for _ in range(depth):
        turtle.forward(side_length)
        draw_side(side_length/3)
        turtle.backward(side_length)
        turtle.right(angle)

# Set up the turtle
turtle.speed(0)  # Set the speed to maximum

# Draw the snowflake
draw_snowflake(100, 6)

# Keep the window
turtle.done()

# Snowflake with Recursion
def draw_snowflake(side_length, depth):
    if depth > 0:
        for _ in range(6):
            turtle.forward(side_length)
            draw_snowflake(side_length/3, depth-1)
            turtle.backward(side_length)
            turtle.right(60)

turtle.speed(0)

draw_snowflake(100, 4)

# Dictionaries
# List Examples (ordered list)
my_list = []

my_list.append("a")
my_list.append("b")
my_list.append("c")

print(my_list)

# Dictionary Methods
my_dict = {}

# Adding a value
my_dict["a"] = 1

print(my_dict)

# Replacing a value
my_dict["a"] = 100

print(my_dict)

# Adding another value
my_dict["b"] = 2

print(my_dict)

# Indexing a value
print(my_dict["b"])

# Removing a value
my_dict.pop("b")

print(my_dict)

# Looping through a dictionary (returns key then value)
my_dict = {"a": 1, "b": 2, "c": 3}

for i in my_dict:
    print(i, my_dict[i])
