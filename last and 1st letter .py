l=[1,2,3,4,5,6]
i=0
b=[]
j=-1
while i<len(l)-3:
    n=l[i]
    v=l[j]
    b.append(v)
    b.append(n)
    j=j-1
    i=i+1
print(b)

