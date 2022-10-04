# l=int(input("enter rhe size"))
# a=[]
# for i in range(l):
#     v=int(input("enter the number:-"))
#     a.append(v)
# for i in range(l):
#     for j in range(0,l,-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

a=[5,4,2,1,3]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j=j+1
    i=i+1
print(a)