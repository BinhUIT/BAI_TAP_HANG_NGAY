n=int(input())
s=0 
dau=1
for i in range (1,3*n+2,1):
    s=s+dau*i 
    dau=-dau
print(s)
