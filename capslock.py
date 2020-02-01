a = input()
n = len(a)
count = 0

for i in a:
	if(i == i.upper()):
		count = count+1

if(n==1 and a == a.lower()):
	print(a.upper())

elif(n==0):
	print(a)

elif (count == n-1 and a[0] == a[0].lower()):
	print(a[0].upper()+a[1:n].lower())

elif count == n:
	print(a.lower())

else:
	print(a)