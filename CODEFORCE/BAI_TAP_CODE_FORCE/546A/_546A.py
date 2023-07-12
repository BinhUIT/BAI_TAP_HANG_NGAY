x,y,z = [int(i) for i in input().split()]
cost = 0
for i in range (1,z+1):
    cost += x*i
if(cost < y):
    print(0)
else:
    print(cost-y)
