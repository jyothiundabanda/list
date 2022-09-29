l=[6,1,3,5]
i=0
p=1
b=[]
while i<len(l):
    if l[i] not in b:
        b.append(l[i])
        p=p*l[i]
    i=i+1
print(b)
print(p)



