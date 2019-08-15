s,u=list(map(int,input().split()))
a=list(map(int,input().split()))
c=0
for i in a:
    if i<=u:
        c+=1
print(c)
