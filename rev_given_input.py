su=input()
l=""
for i in su:
    if i not in l:
        l+=i
print(l[::-1])
