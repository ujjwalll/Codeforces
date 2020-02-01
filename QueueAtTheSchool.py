x,y=input().split()
x=int(x)
y=int(y)

c = input()

d = []

b = ""

for i in c:
	d.append(i)

while (y>0):
	i=0
	while i<(len(d)-1):
		#to check if 'G' is standing behind 'B',If yes thn swap their positions
		if (d[i]=='B' and d[i+1]=='G'):
			d[i],d[i+1]=d[i+1],d[i]
			#as i and i+1 as swapped so it vl be 'B' therefore there is a need to increment
			i+=1
		i+=1
	y-=1

for i in range(len(d)):
	b+=d[i]

print(b)
