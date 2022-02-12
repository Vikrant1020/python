class a:
	def __init__(self,name,age):
		self.name=name
		self.age=age
class b(a):
	def __init__(self,name,age):
		super().__init__(name,age)
		self.classes="7th"
x=b("sagar",13)
print(x.classes)
print(x.name , x.age)