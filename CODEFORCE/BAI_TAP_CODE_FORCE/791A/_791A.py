x,y = [int(i) for i in input().split()]
year = 0
while x <= y:
    x = x*3
    y = y*2
    year+=1
print(year)
