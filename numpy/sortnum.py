import numpy as mn	
a=mn.array([5,1,30,23,4,2])
b=mn.array(['hello','vikrant','welcome','yup!','ankur'])
c=mn.array(['True','False','True'])
d=mn.array([[1,2,3,9],[4,5,1,6]])

# sorting 
print(mn.sort(a))
print(mn.sort(b))
print(mn.sort(c))
print(mn.sort(d))

# filter
# with booln
x=a[[True,False,True,True,False,True]]
print(x)

# filtering using for with a give value.
bool=[]
for no in a:
	if no>20:
		bool.append(True)
	else:
		bool.append(False)

y=a[bool]
print(y)
print(bool)
print('\n')

# filter
tf=a>20
an=a[tf]
print(tf)
print(an)