# set
# loop for a set
a={"hello","vikrant","welcome"}
print(a)
print(type(a))
for x in a:
 print(x)

print("hello" in a)

# add item
a.add("OK")
print(a)

b={"Zero","work","done"}
a.update(b)
print(a)

# can add any type of list in it
c=[67,87,90]
a.update(c)
print(a)

# removing an item
# by using REMOVING to reove an item for a set if the item doesnt in the list then it will show an error. the item tou want to remove must be in the set to be remove.
a.remove("hello")
print(a)

# use discard to remove so it doesnot show any error while removing an item. it exist in the set or not it will remove it.
a.discard("welcome")
print(a)

# joining 2 set. must use a new set for output.
d={67,4356,345,2345,20}
e={54,63,20,345,34,00,67}
f=d.union(e)
print(f)

# also can use update
d.update(e)
print(d)
# both update and union will remove any duplicate item in it.

# intersection
d.intersection_update(e)
print(d)

#for optput in a new variable.
z=d.intersection(e)
print(d)

#symmetric_difference
x={98,89,756,87}
y={78,87,76,8876}
x.symmetric_difference_update(y)
print(x)

# for answer in new vaariable
j=x.symmetric_difference(y)
print(j)