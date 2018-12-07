a=int(input())
count=0
for i in range(a):	
	p,a,v=input().split()
	p=int(p)
	a=int(a)
	v=int(v)
	if (a+p+v>=2):
		count=count+1
print(count)