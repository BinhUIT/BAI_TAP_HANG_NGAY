n = int(input())
temp = input()
Anton = temp.count('A')
Danik = temp.count('D')
if Anton > Danik:
    print("Anton")
elif Danik > Anton:
    print("Danik")
else:
    print("Friendship")

