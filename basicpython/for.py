# for loop
a=("vikrant","ankur",45,56)
for x in a :
 print(x)

# for in word
for x in "vikrant":
	print(x)

# for with break
for x in a:
	if x==45:
		break
	print(x)


# for with continue and range 
# range is the last value for loop.
for x in range(10):
 if x==4:
 	continue
 print(x)


# for loop for single line.
for x in range(5):
	y=x,"hello world"
	print(y)

# for loop in range by defining the range
# range include the first letter of range and remove last letter of range.
for s in range(6,14):
	print(s)

# for loop for in range with increment/decriment in it.
for x in range(2,20,2):
	print(x)

# loop with else.
for x in range(5):
	print(x)
else:
	print("finished")