l=[4, 6, 4, 3, 3,3, 4, 3, 4, 3, 8]
i=0
b=[]
c=[]
k=3
while i<len(l):
    d=l[i]
    if d not in b:
        b.append(d)
        n=l.count(d)
        if n>k:
            c.append(d)
    i=i+1
print(c)

