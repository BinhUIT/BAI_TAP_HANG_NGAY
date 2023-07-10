a,b=[int(x) for x in input().split()]
s=0 
for i in range (a,b+1,1):
    if i%2==0:
        s=s+i 
print(s)
