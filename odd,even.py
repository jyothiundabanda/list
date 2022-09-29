list=[1,2,3,4,5,6,7,8,9,10]
i=0
odd=[]
even=[]
while i<len(list):
    if list[i]%2==0:
        s=list[i]
        even.append(s)
    else:
        d=list[i]
        odd.append(d)
    i+=1
print(odd)
print(even)