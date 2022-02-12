"""for x in range(5,0,-1):
	for y in range(1,6):
		print(x,end=" ")
"""


n=int(input("enter the no. of rows"))
for row in range(n,0,-1):
	for col in range(1,row +1):
		print(col,end=" ")
	print()
	