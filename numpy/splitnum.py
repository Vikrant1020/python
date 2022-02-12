import numpy as nu
a=nu.array([1,2,3,4,5,9,6,7,8,9])
b=nu.array([[1,2,3],[4,5,6]])
c=nu.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# spiliting a array give the array name and no. of array requried form that one array.
d=nu.array_split(a,3)
print(d)
# indexing the new array.
print(d[0])
print(d[1])
print(d[2])
print('\n')

# serching an value in a array.
# give the index value of serched value.
x=nu.where(a==9)
print(x)

# only for 1D
y=nu.searchsorted(a, 7, side='right')

print(y)
