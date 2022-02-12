# sorting strings alphbaticaly.
a=["hello","vikrant","welcome","ankur"]
a.sort()
print(a)

# sorting no. as accending.
b=[34,534,2,0,453,64]
b.sort()
print(b)

#for decending or revers sorting
a.sort(reverse = True)
print(a)
b.sort(reverse=True)
print(b)

# sorting by the nearest no.
def hell(n):
 return abs (n - 100)
b.sort (key=hell)

print(b)

# case sensitive sorting
c=["Zero","Hello","vikrant","apple"]
c.sort()
print(c)

# for removing case sencitive function
c.sort(key=str.lower)
print(c)

# reverse
a.reverse()
print(a)

# copying a list in a new list
d=b.copy()
print(d)


