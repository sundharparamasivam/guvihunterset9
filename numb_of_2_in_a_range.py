su=int(input())
co=0
for i in range(1,su+1):
    a=str(i)
    if "2" in a:
        co+=a.count("2")
print(co)
