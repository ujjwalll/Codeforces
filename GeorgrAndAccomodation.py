a = int(input())

L = []

count = 0

for i in range(a):
	x,y=input().split()
	L.append(int(x))
	L.append(int(y))

i=0

while i<(len(L)):
	s = L[i]
	p = L[i+1]
	if(p-s >= 2):
		count = count + 1
		i = i+2
	else:
		i = i+2

print(count)