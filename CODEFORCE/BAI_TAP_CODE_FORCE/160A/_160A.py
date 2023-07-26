n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort(reverse=True)
sum = 0
for i in range (n):
    sum += arr[i]

tempSum = 0
count = 0
index = 0
while tempSum <= sum:
    tempSum += arr[index]
    sum -= arr[index]
    count+=1
    index+=1
print(count)
