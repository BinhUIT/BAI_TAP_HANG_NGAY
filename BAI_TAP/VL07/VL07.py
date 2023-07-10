n,k=[int(x) for x in input().split()]
s=1
for i in range (0,k,1):
    s=s*(n-i) 
    s=s/(i+1)
print(int(s))
