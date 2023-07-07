numbers=input()
a, b = numbers.split()
a = int(a)
b = int(b)
if (a == 0):
    if (b == 0):
       print('WOW')
    else:
       print('NO')
else:   
     x = "{:.2f}".format(-b/a)
     print(x)
