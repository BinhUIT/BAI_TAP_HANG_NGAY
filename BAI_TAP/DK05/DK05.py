import math
n=int(input()) 
if n<0:
    print('NO')
else:
    m=int(math.sqrt(n)) 
    if((m*m)==n):
        print("YES") 
    else:
        print("NO")
