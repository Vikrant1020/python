import numpy as nd
g=nd.array([1,22,3,4])
d=nd.array([[11,2,3,5],[23,4,2,1]])
e=nd.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# FOR loop in array
# in 1D
for x in g:
	print(x)
print("\n")

# in 2D
for v in d:
	for ac in v:
		print(ac)
print("\n")

# in 3D in 2D.
for m in e:
	print(m)

# 3D in 1D.
for an in e:
	for am in an:
		for aa in am:
			print(aa)
print("\n")

# using function.
for x in nd.nditer(e):
	print(x)

#change datatype wihile iteration.
# need a space for changing datatype we define the space as 'buffered'.
for y in nd.nditer(g, flags=['buffered'], op_dtypes=['S']):
	print(y)
print("\n")

for z in nd.nditer(d[:, ::2]):
	print(z)

# JOINING A ARRAY.
a=nd.array([[1,2,3],[4,5,6]])
b=nd.array([[7,8,9],[10,11,12]])
c=nd.concatenate((a,b))
print(c)
print('\n')
# for joining 2 array with similer positions.
d=nd.concatenate((a,b),axis=1)
print(d)
print('\n')
# using stack
z=nd.stack((a,b),axis=1)
print(z)
print('\n')
# along rows
# no us of axis
y=nd.hstack((a,b))
print(y)
print('\n')
# along coloum
x=nd.vstack((a,b))
print(x)
print('\n')
# along hight depth.
w=nd.dstack((a,b))
print(w)