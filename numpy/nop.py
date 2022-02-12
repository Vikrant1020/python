# numpy for calcuations.
import numpy as nop
a=nop.array([1,2,3,2.8,13])
print(a)
print(type(a))
print(a.dtype)
print("\n")
print(nop.__version__)
print("\n")

# diminsion of a array
b=nop.array(45)
c=nop.array([1,2,3])
d=nop.array([[1,2,3],[1,2,3]])
e=nop.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,12,13]]])
print(b)
print(b.ndim)
print("\n")
print(c)
print(c.ndim)
print("\n")
print(d)
print(d.ndim)
print("\n")
print(e)
print(e.ndim)

#creating diminsions of a array
f=nop.array([1,23,432,1231], ndmin=6)
print(f)
print("number of diminsions",f.ndim)
print("\n")

# indexing of a array
g=nop.array([1,2,3,4,5])
print(g[2])
print(g[1:3],g[2:4])
print(g[1]+g[4])
print(d[0,2])  # for printing the index value of a 2 dminsion array.
print(e[1,1,2])   # for printing the index value of a 3 dminsion array.

# slicing an array
h=nop.array([1,2,3,4,5,6,7,8,9,10])
print(h[1:9:2])    # with skiping element

# converting an array data type
i=nop.array([1,2,3,4,00,5],dtype='S')
print(i)
print(i.dtype)

# changing the datatype of a execting array.
A=a.astype('i')
print(A)
print(A.dtype)

"""
Datatype with there symboles
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

#coping a array in another
x=a.copy()
a[0]=456
print(a)
print(x)
y=x.view()
print(y)

# shape of a array
print(e.shape)
#converting 1D to 2D
z=h.reshape(2,5)
print(z)
# converting into 1D form any Diminsion.
ab=e.reshape(-1)
print(ab)
print("\n")

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


































