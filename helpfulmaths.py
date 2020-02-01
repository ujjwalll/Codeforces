a=input()
c=[]
for i in a:
	if(i.isdigit()):
		c.append(i)
c.sort()
if(len(c)==1):
	print(c[0])
else:
	a=len(c)
	print(c[0],end='')
	for i in range(1,a):
		print('+' + c[i], end='')
		
		
