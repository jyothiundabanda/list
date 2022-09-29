l=[1,2,3,4,5]
i=0
b=[]
while i<len(l):
    d=l[i]
    if d%2==0:
        c=d**2
        b.append(c)
    else:
        k=d
        b.append(k)
    i=i+1
print(b)