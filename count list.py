s="madam"
l=list(s)
l2=[]
count=0
i=0
while i<len(l)-3:
    count=l.count(l[i])
    a=l[i],count
    if list(a) not in l2:
        l2.append(list(a))
    i=i+1
print(l2)