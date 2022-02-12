"""class squre:
	def __init__(self,no):
		self.n=no
		self.side=[o for i in range (no)]

	def inputside(self):
		self.side=[float(input('Enter sides'+str(i+1)+':'))for i range(self.n)]

	def dispside(self):
		for i in range(self.n):
			print('side',i+1,'is',sefl.side[i])


"""
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
s1=Polygon(5)

s1.inputside()
s1.dispside()
