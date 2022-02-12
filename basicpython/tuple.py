# tuple
# you can not modifi a tuple
# to modifi or make a change in tuple you nee dto convert it in list then do modification as sone in list
a=("hello",56,345,"OK", 67)
print(a)
print(type(a))
b=list(a)
print(type(b))
b[1]=("VIKRANT")
a=tuple(b)
print(a)
print(type(a))

# unpacking a tuple
# extrecting items of tuple one by one
# must be smae no. of items in as decleared.
(red,black,green,blue,ok)=a
print(red)
print(black)
print(green)
print(blue)

# to extreact more then one itme in a varialbe.
(x,y,*z)=a
print(x)
print(y)
print(z)