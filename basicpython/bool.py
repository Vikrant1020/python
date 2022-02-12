# Bool (True or False)
a=int(input('enter any number'))
b=int(input('enter second number'))
print(a==b)
print(b>a)
print(a>b)

# with if else
if a>b:
 c="{0} is greater then {1}"
 print(c.format(a,b))
else:
 c="{1} is greater then {0}"
 print(c.format(a,b))

# only empty string and 0 are shown as False all other are true 
print(bool("VIKRANT"))
print(bool(5e6))
print(bool(0))
print(bool())

# other Fasle values are
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""
 
# function that bool is Fasle
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# (isinstance(variable, condition to be true)) aslo use to find a variable is data type
x=24
print(isinstance(x,int))
print(isinstance(x,float))