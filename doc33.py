l=[12, 67, 98, 34]
i=0
b=[]
while i<len(l):
    sum=0
    if l[i]>0:
        r=l[i]%10
        sum=sum+r
        l[i]=l[i]//10
    b.append(sum)
    i=i+1
print(b)


# l=[12, 67, 98, 34]
# i=0
# b=[]
# while i<len(l):
#     sum=0
#     while l[i]>0:
#         r=l[i]%10
#         sum=sum+r
#         l[i]=l[i]//10
#     b.append(sum)
#     i=i+1
# print(b)