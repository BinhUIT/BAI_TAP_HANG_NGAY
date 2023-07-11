a=input()
arr="hello"
ind=0
flag=0
for i in range (0,len(a),1):
    if(a[i]==arr[ind]):
        ind=ind+1
        if ind==5:
            flag=1
            break
if flag==1:
    print("YES")
else:
    print("NO")