# your code goes here
import math
x,y = input().split()
x = int(x)
y = int(y)
even = 2
odd = 1
k = math.ceil(x/2)
if(k<y):
	print(2*(y-k))
elif(y==1):
	print(1)
elif(k>y and x%2 == 0):
	print(x-(1+(2*(k-(y)))))
elif(k==y and k%y==0 and x%2==0):
	print(x-1)
elif(k==y and k%y==0 and x%2!=0):
	print(x)
elif(x%2!=0):
	c = x+1
	print(c-(1+(2*(k-(y)))))
else:
	print(1+(2*(k-(y))))