x = input()
count = x.count('4')
count += x.count('7')
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")