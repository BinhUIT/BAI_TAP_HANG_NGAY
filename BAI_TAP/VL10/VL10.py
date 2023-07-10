n=int(input())
s=0
if n!=0:
    n=abs(n)
    while(n!=0):
        n=n//10
        s=s+1
    print(s)
else:
    print(1)