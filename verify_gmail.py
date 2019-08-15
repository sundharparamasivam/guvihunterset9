su=input()
a=su[:su.index("@")]
if "@gmail.com" in su and len(a)>2:
    print("YES")
else:
    print("NO")
