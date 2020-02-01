n = int(input())
a = [0]*n
k = 0
for i in range(0,n):
    a[i] = int(input())
for i in range(1,n):
    if a[i-1] != a[i]:
        k += 1
print(k+1)