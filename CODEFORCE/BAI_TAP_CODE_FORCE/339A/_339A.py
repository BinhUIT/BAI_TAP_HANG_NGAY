n=input()
t1=t2=t3=""
for i in range(0,len(n),1):
    if(n[i]=="1"):
        t1=t1+"+1"
    if(n[i]=="2"):
        t2=t2+"+2"
    if(n[i]=="3"):
        t3=t3+"+3"
t=t1+t2+t3 
for i in range(1,len(t),1):
    print(t[i],end="")