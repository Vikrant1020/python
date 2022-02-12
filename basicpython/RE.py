# reguler expension.
import re
a=("hello my name is vikrant. m from hisar, HBC.")
x=re.search("^hello.*HBC.$",a)
if x: 
	print("yes")
else:
	print("no")


c=input("enter your name:")
print("my name is "+c)