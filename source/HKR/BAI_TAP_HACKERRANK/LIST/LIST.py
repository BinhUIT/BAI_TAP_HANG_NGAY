import array as arr
def main(x,y,z,n):
    i=0
    res1=arr.array('i')
    res2=arr.array('i')
    res3=arr.array('i')
    while(i<=x):
        j=0
        while(j<=y):
            k=0
            while(k<=z):
                if(i+j+k!=n):
                    res1.append(i)
                    res2.append(j)
                    res3.append(k)
                k=k+1
            j=j+1
        i=i+1
    return res1, res2, res3
if __name__=='__main__':
    x=int(input())
    y=int(input())
    z=int(input())
    n=int(input())
    res1,res2,res3=main(x,y,z,n)
    s=len(res1)
    i=0
    print("[", end='')
    while(i<s):
       if(i==s-1):
           print("[",res1[i],",",res2[i],",",res3[i],"]]", sep='')
       else:
           print("[",res1[i],",",res2[i],",",res3[i],"],",sep='', end='')
       i=i+1
    
   


