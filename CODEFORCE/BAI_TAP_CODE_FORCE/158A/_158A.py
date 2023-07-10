n,k = [int(x) for x in input().split()]
 #To input array in 1 line
arr = list(map(int, input().split()))
#Count until enough winner
count = 0
while count < k:
    if(arr[count] > 0):
        count+=1
    else: break

 #If occur when exist 0 point
if(count < k):
    print(count)
else:
    index = count-1
    for i in range (count,n):
        if arr[i] == arr[index]:
            count+=1
    print(count)
