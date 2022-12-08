import turtle
win = turtle.Screen()
turtle.shape("turtle")
turtle.pensize(3)

for i in range(4):
  turtle.forward(100)
  turtle.right(90)

for i in range(4):
    turtle.forward(80)
    turtle.left(120)

win.mainloop()


