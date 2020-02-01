import collections

x,y=input().split()
x = int(x)
y = int(y)

c=list(map(int, input().split()))

d = collections.deque()

hu = []

for i in c:
	if i not in d:
		d.appendleft(i)


for i in d:
	hu.append(i)

po = hu[-y:]

print(len(po))

for i in po:
	print(i, end = " ")
