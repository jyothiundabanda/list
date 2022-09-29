a=["t","a","m","m","a","n","a"]
b=[]
i=0
c=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c=c+1
    i=i+1
print(c)
print(b)



