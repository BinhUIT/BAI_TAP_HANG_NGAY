x,n=[float(x) for x in input().split()]
n=int(n)
s=0 
tu=1
mau=1
for i in range (1,n+1,1):
    tu=tu*x 
    mau=mau*i
    s=s+tu/mau
print("{:.2f}".format(s))
