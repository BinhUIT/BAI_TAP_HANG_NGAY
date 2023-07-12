a = input()
result = {} #map in python
for i in a:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
count = 0
if len(result) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
