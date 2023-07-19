n = int(input())
capacity = 0
max = capacity
for i in range (n):
    x,y = [int(i) for i in input().split()]
    capacity -= x
    capacity += y
    if capacity > max:
        max = capacity
print(max)
