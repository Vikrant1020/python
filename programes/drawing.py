import turtle
t=turtle.Turtle()
t.shape("turtle")
t.screen.bgcolor("black")
t.color("yellow")
t.setheading(45)
t.pensize(5)
for x in range(1,100,2):
	t.forward(x+1)
	t.left(40)
turtle.done()