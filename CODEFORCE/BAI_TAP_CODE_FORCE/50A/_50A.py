m,n = [int(x) for x in input().split()]
maxRange = m*n
for i in range (m*n,-1,-1):
    if i % 2 == 0:
        print(i//2)
        break
