su=list(input().split())
j=0
l=[]
if "."in su:
    su.remove(".")
for i in su:
    if "."in i:
        i=i[:-1]
    j+=1
    if j%2!=0:
        l.append(i[::-1])
    else:
        l.append(i)
print(*l)
