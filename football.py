a=input()
flag = 0
flag1=0
count=0
count2=0
for i in a:
	if(i=='1'):
		count2=0
		count = count+1
		if(count>=7):
			flag = 1
	if(i=='0'):
		count=0
		count2 = count2 +1
		if(count2>=7):
			flag1=1
if(flag==1 or flag1==1):
	print("YES")
else:
	print("NO")
