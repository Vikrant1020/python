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
for n in range(1,13):
	t.penup()
	t.right(360/12)
	t.fd(180)
	t.write(n)
	t.goto(0,0)

def harm():
	t.penup()
	t.left(90)
	t.pendown()
	t.pensize(3)
	t.fd(100)
	t.home()

def marm():
	t.penup()
	t.left(90)
	t.pendown()
	t.pensize(3)
	t.fd(140)
	t.home()
harm()
marm()
t.left(90)
t.home()
for x in range(0,3600,6):
	t.home()
	t.right(-90+x)
	t.down()
	t.fd(100)
	time.sleep(1)
	t.undo()
	
turtle.done()










