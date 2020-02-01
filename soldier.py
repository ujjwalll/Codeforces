k = input().split(" ")
a = int(k[0])
b = int(k[1])
c = int(k[2])
e = 0

e = ((c*(c+1)) * a)/2

f = e - b
f = int(f)
if(f<0):
	print(0)
else:
	print(f)