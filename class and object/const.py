class compnum:
	def __init__(self,r=0,i=-1):
		self.real=r
		self.imagner=i
	def combine(self):
		print(f'{self.real}+{self.imagner}j')

num10=compnum(2,3)										# giving the attribute for default funcyions __init__.

num10.combine()											# calling function.

num20=compnum(5)

num20.combine()

num20.attre=num10										# for ceating a new attribute. 

print((num20.real,num20.imagner,num20.attre))			# for printing one attribute's
