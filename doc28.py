l=[1, 1, 2, 3, 4, 5, 1, 2]
i=0
b=[]
while i<len(l):
    d=l[i]
    if d!=1:
        b.append(d)
    i=i+1
print(b)