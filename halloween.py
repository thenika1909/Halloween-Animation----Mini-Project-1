from turtle import *
import turtle

t=turtle.Turtle()
screen=turtle.Screen()
screen.setup(900,670)
screen.bgcolor('black')
t.speed(50)
t.hideturtle()
t.fillcolor('#DC5F00')
t.begin_fill()
t.up()
r=180
t.goto(0,-240)
t.circle(r)
t.end_fill()
t.up()
t.setpos(-140,-45)
t.fillcolor('gold')
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

t.up()
t.setpos(90,40)
t.fillcolor('gold')
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

t.up()
t.setpos(0,-110)
t.fillcolor('gold')
t.begin_fill()
t.forward(40)
t.right(120)
t.forward(40)
t.right(120)
t.forward(40)
t.end_fill()

t.up()
t.setpos(-60,-120)
t.fillcolor('gold')
t.begin_fill()
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()

t.up()
t.setpos(-60,-120)
t.fillcolor('gold')
t.begin_fill()
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()

t.up()
t.setpos(14,-163)
t.fillcolor('gold')
t.begin_fill()
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()

t.up()
t.setpos(90,-120)
t.fillcolor('gold')
t.begin_fill()
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()

t.fillcolor('green')
t.begin_fill()
t.goto(-20,110)
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.end_fill()
t.goto(-250,-290)
t.pencolor('red')
screen.mainloop()
