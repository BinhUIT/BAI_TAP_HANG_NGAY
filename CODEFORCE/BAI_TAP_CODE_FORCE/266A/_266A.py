y = int(input())
x = input()
count = 0
for i in range(0,len(x)-1):
    if x[i] == x[i+1]:
        count+=1
print(count)   

#CHEATED (Dont feel logical enough - but correct though)
