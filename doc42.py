l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
b=[]
c=[]
while i<len(l):
    d=l[i]
    if d>=l[3]:
        b.append(d)
    else:
        c.append(d)
    i=i+1
    k=b+c
print(k)
