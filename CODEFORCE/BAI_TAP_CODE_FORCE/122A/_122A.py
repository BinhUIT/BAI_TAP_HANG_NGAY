arr=[4,7,44,47,74,77,444,447,474,744,774,747,477,777]
n=int(input())
flag=0
for i in range(0,len(arr),1):
    if n%arr[i]==0:
        flag=1
if flag==1:
    print("YES")
else:
    print("NO")