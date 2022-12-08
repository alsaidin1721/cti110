import turtle
snow = turtle.Turtle()

turtle.Screen().bgcolor("grey")
colors = ["cyan", "purple", "white", "blue"]

snow.pencolor("blue")
snow.penup()
snow.forward(90)
snow.left(45)
snow.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            snow.forward(30)
            snow.backward(30)
            snow.right(45)
        snow.left(90)
        snow.backward(30)
        snow.left(45)
    snow.right(90)
    snow.forward(90)

for i in range(8):
    branch()
    snow.left(45)

# snow.color(random.choice(colors))
        
