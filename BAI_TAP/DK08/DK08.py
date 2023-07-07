a = input().split()
x = float(a[0])
y = float(a[2])

if(a[1] == '+'):
    print("{:.2f}".format(x+y))
elif (a[1] == '-'):
    print("{:.2f}".format(x-y))
elif (a[1] == '*'):
    print("{:.2f}".format(x*y))
elif (a[1] == '/'):
    if(y == 0):
        print("Math Error")
    else:
        print("{:.2f}".format(x/y))
