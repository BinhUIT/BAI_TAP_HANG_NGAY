





a=float(input()) 
if(a>0):
    s=int(a)
    if(a>=s+0.5):
        a=s+1
    else:
        a=s 
if(a<0):
    s=int(a)
    if(a>s-0.5):
        a=s 
    else:
        a=s-1 
print(a)
