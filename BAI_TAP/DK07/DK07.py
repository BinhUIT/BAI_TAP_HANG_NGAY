import math
a, b, c = [int (x) for x in input().split()]
if (a == 0 and b != 0 and c != 0):
    xn = -c / b
    print("{:.2f}".format(xn))
elif (a == 0 and b == 0 and c != 0):
    print("NO")
elif (a == 0 and  b == 0 and c == 0):
    print("WOW")
elif (a == 0 and b != 0 and c == 0):
    print("0.00")
else:
    d = b * b - 4 * a * c
    if (d <= 0):
        if (d == 0):
            x = (-b) / (2 * a)
            print("{:.2f}".format(x))
        else:
            print("NO")
    else:
         x1 = (-b - math.sqrt(d)) / (2 * a)
         x2 = (-b + math.sqrt(d)) / (2 * a)
         print("{:.2f}".format(x1),"{:.2f}".format(x2))