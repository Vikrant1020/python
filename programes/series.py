i=int(input("enter the no. values requered"))
a=int(input("enter first value"))
print(a)
b=a+1
print(b)
d=0
for x in range(1,i+1):
	c=a+b
	a=b
	b=c
	print(c)
	d=d+c
print("sum of the series is",d)