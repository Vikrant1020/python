import turtle
import time
t=turtle.Turtle()
t.speed(9)
x=0
y=0

t.write((x,y))
t.home()
y=-200
t.penup()
t.goto(x,y)
t.pendown()
t.begin_fill()
t.fillcolor("orange")
t.circle(200)
y=-150
t.penup()
t.goto(x,y)
t.pendown()
t.circle(150)
t.end_fill()
t.penup()
t.home()
t.left(90)
for n in range(1,61):
	t.penup()
	t.right(360/60)
	t.fd(180)
	t.write(n)
	t.goto(0,0)

t.left(90)
t.home()
for marm in range(0,360,6):
	t.home()
	t.pensize(3)
	t.right(-90+marm)
	t.down()
	t.color("green")
	t.fd(140)
	t.penup()
	t.backward(140)
	for x in range(0,361,6):
		t.home()
		t.right(-90+x)
		t.down()
		t.color("black")
		t.fd(100)
		time.sleep(1)
		t.undo()
	time.sleep(0)
	t.undo()
turtle.done()










