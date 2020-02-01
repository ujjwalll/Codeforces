# your code goes here
x,y = input().split()
x = int(x)
y = int(y)
count = 0
k = list(map(int, input().strip().split()))
for i in k:
	if(i>y):
		count = count+2
	else:
		count = count+1
print(count)
