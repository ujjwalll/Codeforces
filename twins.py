a = int(input())
b = list(map(int, input().split())) 
count = 0


b.sort(reverse = True)

Sum = sum(b)

half = Sum/2
d=0

for i in range(a):
	d = d+b[i]
	count = count + 1
	if(d>half):
		print(count)
		break;