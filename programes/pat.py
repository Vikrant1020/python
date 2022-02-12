z=6
for i in range(7):
	for k in range(z):
		print(end=' ')
	z-=1
	for j in range(0,i):
		print('*',end=' ')
	print('')
t=1
for i in range(5,0,-1):
	for k in range(t):
		print(end=' ')
	t+=1
	for j in range(i):
		print('*',end=' ')
	print('')
