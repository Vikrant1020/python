# if else
# elif is used to use anothe condition in else.
a=56
b=450
if a>b:
 print("a is grester then b")
elif a < b:
 print("b is greater then a")

# else donot contain any condition.
# else if is known as elif.
c=45
d=45
if c<d:
	print("c id gretater then d")
elif c>d:
	print("d is greater then c")
else:
	print("both are equal")


# another way to use if else.
print("C") if c>d else print("D") if c<d else print("=")

#both condition should be true
x=45
y=34
z=61
if x>y and x>z:
	print("x is bigest")
elif y>x and y>z:
	print("y is bigest")
else:
	print("z is bigest")


# one condiotion shoul be true
g=45
h=65
if g==h or g<h:
	print("g is greater then h")

i=45
if i>34:
 print("34")
 if i>40:
  	print("biger then 34")
 else:
  	print("smaller then 34")




