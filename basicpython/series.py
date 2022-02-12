#febonice series.
# repation a function in itself.
def add(x):
	if (x>-1):
		result= x + add(x-1)
		print(result)
	else:
		result=0
	return result


print("answer is")
add(7)