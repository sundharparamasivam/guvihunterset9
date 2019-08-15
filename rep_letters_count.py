su=list(input())
l=""
j=-1
c=1
for i in range(1,len(su)):
    j+=1
    if su[j]==su[i]:
        c+=1
    elif c>1:
        l+=str(c)+"*"+str(su[j])
        c=1
    else:
        l+=str(su[j])
        c=1
if c>1:
    l+=str(c)+"*"+su[-1]
else:
    l+=su[-1]
print(l)
