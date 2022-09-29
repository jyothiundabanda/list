l=[5, 6, [], 3, [], [], 9]
i=0
b=[]
while i<len(l):
    d=l[i]
    if d!=[]:
        b.append(d)
    i=i+1
print(b)
