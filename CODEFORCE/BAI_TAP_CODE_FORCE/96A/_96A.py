a=input()
s=0
flag=0
for i in range(1,len(a),1):
    if a[i]==a[i-1]:
        s=s+1
        if s==6:
            flag=1
            break
    else:
        s=0
if flag==1:
    print("YES")
else:
    print("NO")