from itertools import count


l= [2, -7, 5, -64, -14]
i=0
count=0
t=0
b=[]
while i<len(l):
    d=l[i]
    if d>=0:
        b.append(d)
        count=count+1
    else:
        b.append(d)
        t+=1
    i=i+1
print(count)
print(t)
