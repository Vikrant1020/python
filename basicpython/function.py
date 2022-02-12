#function 
#function with a variable name.(hello)
def add(hello):
 print(hello+" vikrant")
add("ankur")
add("ok")
add("hell")
print("\n")


# for giving variable name and give value at the time of call of function.(k,r)
def ok(k,r):
	print(k+" "+r)
ok("kite","RAM")
print("\n")


# for multiple values in a singlr  function.
# must konw the position of value we need. because it will print only one value out of your tulpe.
def HMM(*kids):
	print("HELOO"+kids[0])
HMM("ankur", " vikrant")
print("\n")


#same as above.
def son(old,young):
	print("old one is"+old)
son(old="vikrant",young="ankur")
print("\n")


# more attribute,s
def fam(**home):
	print("my hme is in "+home["frb"])
fam(hisar="663 HBC hisar",frb="metro")
print("\n")


# for giving a default parameter.
# hear india is a default country name.
def con(country="INDIA"):
	print("my home town is in "+country)
con("pak")
con()
con("canada")
print("\n")

# for loop in function.
def eat(food):
	for x in food:
		print(x)
number=["ok","hmm"]
a=(78,46,89)
eat(number)
eat(a)
print("\n")


# returen a value of a function.
# the value will returen as given in returen function.
def add():
	x=int(input('enter any number'))
	return 3*x
print(add())











