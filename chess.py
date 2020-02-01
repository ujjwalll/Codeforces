# your code goes here
a = int(input())
s = input()

count = 0
count1 = 0

for i in s:
	if(i=="A"):
		count = count +1
	elif(i=="D"):
		count1 = count1+1

if(count>count1):
	print("Anton")
elif(count1>count):
	print("Danik")
else:
	print("Friendship")
