a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
b=[]
while i<len(a):
    if type (a[i])==int and a[i]>=0:
        b.append(a[i])
    i=i+1
print(b)


l=[12, 67, 98, 34]
# i=0
# b=[]
# while i<len(l):
#     sum=0
#     r=l[i]%10
#     l[i]=l[i]//10
#     a=r+l[i]
#     b.append(a)
#     i=i+1
# print(b)