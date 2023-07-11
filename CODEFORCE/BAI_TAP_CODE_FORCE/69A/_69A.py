n = int(input())
a1=b1=c1=0
for i in range (0,n):
    a,b,c=[int(x) for x in input().split()]
    a1=a1+a 
    b1=b1+b 
    c1=c1+c
if a1==0 and b1==0 and c1==0:
    print("YES")
else:
    print("NO")