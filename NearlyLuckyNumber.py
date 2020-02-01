a = input()

l=[]

count = 0

for i in a:
	l.append(int(i))

for i in range(len(a)):
	if(l[i]==4 or l[i]==7):
		count = count+1

if(count == 0):
	print("NO")

elif(count==4 or count==7):
	print("YES")
else:
	print("NO")