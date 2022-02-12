row=int(input('enter the no of rows'))

def main(row):

	a=[ ]
	for i in range(row):
		no=i+1
		a.append(no)
	#print(a[-1])
	def ok(row):
		for i in range(row):
			print(a[i],end=' ')
		a.reverse()
		for i in range(1,len(a)):
			print(a[i],end=' ')
	ok(row)
	#print('')
#main()
z=0
for i in range(row):
	for k in range(z):
		print(end=' ')
	z+=2
	for j in range(1):
		main(row)
		#print('\n',end=' ')
	row-=1	
	print('')