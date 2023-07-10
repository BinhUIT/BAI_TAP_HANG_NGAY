n = int(input())
count=0
for i in range (0,n):
    numbers=input()
    a, b ,c= numbers.split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b+c>=2:
        count+=1
print(count)
