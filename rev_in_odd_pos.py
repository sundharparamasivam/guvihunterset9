su=list(input().split())
j=0
l=[]
for i in su:
    j+=1
    if j%2!=0:
        l.append(i[::-1])
    else:
        l.append(i)
print(*l)
