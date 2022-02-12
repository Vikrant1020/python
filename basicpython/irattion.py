# irattion
# iter is used for making a tuple or string itratable
# to use itration next is used.
# itration on a tuple.
a=("hello","vikrant","zero")
b=iter(a)
c=len(a)
for x in range(c):
	print(next(b))


# itration on a string.
x="vikrant"
y=iter(x)
z=len(x)
for irt in range(z):
	print(next(y))

"""
# making a itration
class no:
	def __iter__(self):
		self.x=1
		return self
	def __next__(self):
		a=self.x
		self.x*=2
		return a
myclass=no()
hello=iter(myclass)
for g in range(10):
	print(next(hello))
print("\n")

# stoping an itrartion.
class ok:
	def __iter__(self):
		self.x=1
		return self
	def __next__(self):
		if self.x<=1025:
			a=self.x
			self.x*=2
			return a
		else:
			raise StopIteration
myclass=ok()
so=iter(myclass)
for i in so:
	print(i)




"""