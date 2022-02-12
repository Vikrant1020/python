# calss and object
class ok:
	def __init__(self,name,age):
		self.name=name
		self.age=age
name=str(input('enter name'))
age=int(input('ente age '))
E1=ok(name,age)
E2=ok(name,age)
print(E1.name, E1.age)
print(E2.name,E2.age)
print("\n\n")
"""
# for exmpla
class clas:
	def __init__(self,name,cours,age):
		self.name=name
		self.age=age
		self.cours=cours
s1=clas("AK",20,"Bsc(CA)")
s2=clas("VK",21,"Bsc(CS)")
s3=clas("RK",21,"bse(non-medi")
print(s1.name,s1.age,s1.cours)
print(s2.name,s2.age,s2.cours)
print(s3.name,s3.age,s3.cours)
print("\n")

#function in a class.
class comp:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def nam(self):
		print("employ name is "+self.name+"and he is ",self.age,"years old")
e1=comp("vikrant",20)
e2=comp("ankur",21)
print(e1.name)
# for deleting object.
del e2
e1.nam()
print("\n")

# using differnet attrebute in function.
class compy:
	def __init__(ok,name,age):
		ok.name=name
		ok.age=age
	def hello(hel):
		print("name is :"+hel.name)
f1=compy("AK",20)
#for modifiying 
f1.name=("VK")
f1.hello()
print("\n")

# parent class and a child class.
class i:
	def __init__(self,name, age):
		self.name=name
		self.age=age
	def o(self):
		print(self.name+self.age)
class p(i):
	pass
x=p("sagar",13)
print(x.name,x.age)


"""












