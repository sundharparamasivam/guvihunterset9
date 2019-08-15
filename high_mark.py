su=list(input().split("#"))
su1=list(input().split("#"))
s=0
s1=0
for i in range(1,len(su)):
    s+=int(su[i])
for j in range(1,len(su1)):
    s1+=int(su1[j])
if s>s1:
    print(su[0])
else:
    print(su1[0])
