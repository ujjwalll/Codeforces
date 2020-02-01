a = int(input())
b = int(input())
c = int(input())

p = a*b*c
q = (a+b)*c
r = a*(b+c)
s = a+b*c
t = a+b+c
u = a*b+c

print(max(p,q,r,s,t,u))