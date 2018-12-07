a,y=input().split()
a=int(a)
y=int(y)
b = [int(x) for x in input().split()]
count = 0
y=int(y)
for i in range(len(b)):
	if b[i]>=b[y-1] and b[i]>0:
		count=count+1
print(count)