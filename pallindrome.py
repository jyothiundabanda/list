l=['j','y','o','o','y','j']
i=0
s=0
while i<len(l):
    n=l[i]
    r=n[::-1]
    if l[i]==r:
        print(r,"pallindrome")
        s=s+1
    else:
        print(r,"not")
    i=i+1


