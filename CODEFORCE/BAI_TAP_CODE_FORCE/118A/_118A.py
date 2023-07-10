chuoi=input()
res=""
chuoi=chuoi.lower()
for i in range(0,len(chuoi),1):
    if(chuoi[i]!='a'and chuoi[i]!='o'and chuoi[i]!='i'and chuoi[i]!='u' and chuoi[i]!='e' and chuoi[i]!='y'):
        res=res+'.'+chuoi[i]
print(res)
