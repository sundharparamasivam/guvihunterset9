su=list(input().split())
l=[]
s=1
for i in range(len(su)):
    l.append(su[-s])
    s+=1
print(*l)
