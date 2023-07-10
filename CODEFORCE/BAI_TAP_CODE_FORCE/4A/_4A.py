x = int(input())
if (x%2 !=0):
    print("NO")
else:
    for i in range (2,x-1,2):
        if((x-i) % 2 == 0):
            print("YES")
            break;
    else:
        print("NO")
