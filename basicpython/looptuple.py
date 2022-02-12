# loop in tuple
# for printing a tuple item by item.
a=(67,"hello",67,"world",67)
for x in a:
 print(x)
print("\n\n\n")

# for loop with range.
for i in range(len(a)):
	print(a[i])

# while loop
i=0
while i < len(a):
 print(a[i])
 i=i+1

# joining or multiplying item in a tuple.
c=("hello",67,"vikrant")
d=("OK",56,"SORRY")
e=c+d
print(e)
c=c*2
print(c)

# for finding position of item in a tuple
x=a.index(67)
print(x)

# for counting an item how many time it come in a tuple.
y=a.count(67)
print(y)