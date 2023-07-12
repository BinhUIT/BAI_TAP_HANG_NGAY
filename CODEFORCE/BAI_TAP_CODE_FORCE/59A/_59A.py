x = input()
uppercase = 0
for i in x:
    if i.isupper():
        uppercase+=1
lowercase = len(x)-uppercase
if uppercase > lowercase:
    x = x.upper()
else:
    x = x.lower()
print(x)
