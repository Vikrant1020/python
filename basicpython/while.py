# while loop
a=1
while a < 6:
 print(a)
 if a==4:
  break
 a=a+1

print("\n\n")

# using continue statement.
# for skiping the value requried.
b=0
while b < 6:
 b=b+1
 if b==3:
	 continue
 print(b)
print("\n\n")

#using else in while.
c=1
while c<4:
 print(c)
 c=c+1
else :
	print("c is no longer bigger then 4 ")