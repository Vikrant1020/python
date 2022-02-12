# for finding a word in string ans will be (true or false not the position)
a= str(input('enter your data\n'))
print("hello" in a)

# must enter data in other variable to using it in if else or loop. 
b=a;

# check with looop.
if "I am " in b:
	print("yes, I am is in a")

# check if not there
print("ANKUR" not in a)


if "ANKUR" not in a:
	print("ANKUR is not present")