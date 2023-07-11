n,k=[int(x) for x in input().split()]
for i in range(0,k,1):
    dv=n%10
    if dv==0:
        n=n/10
    else:
        n=n-1
print(int(n))