a=int(input())
for i in range(a):
	b=input()
	c=len(b)
	if c > 10:
		print(str(b[0])+str(c-2)+str(b[c-1]))
	else:
		print(b)
