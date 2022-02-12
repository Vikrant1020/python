# lamba
# a single line function is known as lambda
z= lambda x,y: x*y
print(z(4,7)) 

# lambda in a function
def x(n):
	print("hello")
	return lambda a: a*n
n=int(input('enter the value of n'))
a=int(input('enter the value of a'))
z=x(n)
print(z(a))

# when a function value is not same then we use lambda in return for differenrt function value.
def y(n):
	return lambda a: a*a/n
g=y(5)
h=y(10)
print(g(5))
print(h(5))