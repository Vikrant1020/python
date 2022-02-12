# for importing a another file as in yours.
# import is used and after that name of file to be import.
"""import model
model.name("vikrant")

# importing a list and printing a sepicifi value.
import model
a=model.student["age"]
b=model.student["class"]
print(a)
print(b)

# changing th file name as you want to import.
import model as ak
c=ak.name("vikrant")
"""

# default imoprt.
import platform
d=platform.system()
print(d)

e=dir(platform)
print(e)


"""
#for importing a sepicific type of data form another file.
from model import student
print(student["age"])

# for day time
import datetime
y=datetime.datetime.now()
print(y)
print(y.year)
print(y.month)
print(y.day)
# %A for day 
print(y.strftime("%A"))
# %B for month
print(y.strftime("%B"))
# %c for date
print(y.strftime("%C"))

"""










