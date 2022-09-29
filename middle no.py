a=[6,8,5,4,6,9]
i=0
while i<len(a)/2:
    if len(a)%2==0:
        g=a[i]
        h=a[i+1]
    i=i+1
print(g,h)


# a=[6,8,5,4,6,9]
# i=0
# v=[]
# while i<len(a)-1:
#     v.append(a[i+1])
#     v.append(a[i])
#     i=i+2
# print(v)