n = int(input())
allRooms = []
for i in range (n):
    allRooms.append(list(map(int,input().strip().split())))

count = 0
for i in range(n):
        if (allRooms[i][1] - allRooms[i][0]) >=2:
            count+=1
print(count)

