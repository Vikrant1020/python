# loop in list 
# to show all item in list one by one.
a=["sorry","vikrant","welcome","ankur","world", "welcome"]
for x in a:
 print(x)

# full list shown with same number of item's in it. 
for i in range(len(a)):
 print(a)

# with while loop.
i=0
while i < len(a):
 print(a[i])
 i=i+1

# another way to use for loop.
[print(x) for x in a] 
print('\n\n')

# for adding a unique type of item form on list to another.
# we added the items that contain letter "o" in it.
b=["ANKUR"]
for y in a:
  if "o" in y:
    b.append(x)

print(b)

# another way to a unique item in new list.
c=[x for x in a if "e" in x]
print(c)

# removing an item from form a list. 
d=[x for x in a if x != "ankur"]
print(d)

# loop in list
e=[x for x in range(14)]
print(e)

# condition in 
f=[x for x in range(50) if x < 39]
print(f)

g=[x for x in range(50) if x < 50/2]
print(g)

# change output 
h=["ok" for x in a]
print(h)

# cahnge all items in list of same value
i=[x if x!="welcome" else "DONE" for x in a]
print(i)