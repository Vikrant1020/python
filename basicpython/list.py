# for list
a=["ankur",56,"vikrant",True, "welcome"]
print(a)
print(len(a))
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
print(a[:1])
print(a[2:])
if "ankur" in a:
	print("yes")


# for changing an item in list.
a[2]="VIKRANT"
print(a)
a[1:3]=["hello","world"]
print(a)
a[3:4]=["OK","come"]
print(a)
a[0:3]=["SORRY"]
print(a)

# insert new item in list.
a.insert(0,"ANKUR")
print(a)
a.append("yes")
print(a)

# merging 2 list in one
b=[45,64,"3r5"]
print(b)
a.extend(b)
print(a)

# removing items
a.remove("3r5")
print(a)
a.pop(2)
print(a)
a.pop() # for last item in list
print(a)
del a[0]
print(a)

""" for deleting a compleate list
del b
print(b)
"""

# for deletig all items in a still list remain same with out any item in it.
a.clear()
print(a)


