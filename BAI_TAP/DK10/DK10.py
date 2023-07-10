import array as arr 
m,y = [int(x) for x in input().split()]
if y<=0 or y>100000 or m<1 or m>12:
    print('INVALID')
else:
    a = arr.array('i', [0,31,28,31,30,31,30,31,31,30,31,30,31]) 
    if (y%400==0) or (y%4==0 and y%100!=0):
        a[2]=29 
    print(a[m])
