a=int(input('1st no.'))
b=int(input('2nd no.'))
c=b-a
for i in range(c):
	for j in range(11):
		print(a,'*',j,'=',a*j)
	a=a+1
	