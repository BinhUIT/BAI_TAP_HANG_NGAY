n = int(input())
result = 0
for i in range (0,n):
     temp = input()
     if( temp == "++X" or temp == "X++"):
         result+=1
     elif temp == "--X" or temp == "X--":
         result-=1
print(result)
