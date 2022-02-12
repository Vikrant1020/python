# dictionary
a={
	"name":str(input('enter name')),
	"age": int(input('enter age')),
	"age": 21,
	"class":str(input('enter class'))
}
# any duplicate key word will over write the old.
print(a)
print(type(a))
print(a["name"])
print(len(a))
b=a["class"]
print(b)
y=a.get("name")
print(y)
print('\n\n')

#for all key words in dict
z=a.keys()
print(z)
print('\n\n')

# for all values.
w=a.values()
print(w)
print('\n\n')

#adding a key an value
a["attan"]=int(input('enter your attendance'))
print(z)
print(a)
print('\n\n')


# for all items of dict
b=a.items()
print(b)
print('\n\n')

"""
# for removing an item
a.pop("age")
print(a)
"""

# from keys makes all same values different keys
h=("name","age","rollno.")
j=("vikrant",20,328612978)
l=dict.fromkeys(h,j)
print(l)
