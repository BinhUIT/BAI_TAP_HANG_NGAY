matrix = []
for i in range (0,5):
    matrix.append([int(j) for j in input().split()])
step = 0
#Find index of 1 value
for i in range (0,5):
    for j in range (0,5):
        if(matrix[i][j] == 1):
            step = abs(i-2) + abs(j-2)
            break;
print(step)