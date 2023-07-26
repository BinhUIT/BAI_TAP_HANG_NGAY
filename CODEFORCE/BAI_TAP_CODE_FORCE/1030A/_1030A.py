n = int(input())
a = list(map(int, input().strip().split()))
for i in range (n):
    if a[i] == 1:
        print("HARD")
        break
else: print("EASY")