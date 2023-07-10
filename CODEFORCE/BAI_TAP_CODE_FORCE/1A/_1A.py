numbers=input()
n,m,a= numbers.split()
n = int(n)
m = int(m)
a = int(a)
tmp = int(n/a)*int(m/a)
if(n%a!=0):
    tmp=tmp+int(m/a)+1
if(m%a!=0):
    tmp=tmp+int(n/a)+1
if(n%a!=0 or m%a!=0):
    tmp=tmp-1
print(tmp)
