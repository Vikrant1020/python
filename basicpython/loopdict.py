a={
	"name":"vikrant",
	"age":20,
	"roll._no.":183112320012
}
print(a)
for x in a:
	print(a)

# for value's
for x in a:
	print(a[x])

print("\n\n")

for x in a.keys():
	print(x)
print("\n\n")

for x,y in a.items():
 print(x,y)

print("\n\n")
for x in a.values():
 print(x)
print("\n\n")

b=a.copy()
print(b)