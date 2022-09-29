l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=l[i]
while i<len(l):
    d=len(l[i])
    e=len(l[i])
    if d>e:
        e=d
    if l[i]>max:
        max=l[i]
    i=i+1
l=e,max
print(l)


# l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# min=l[i]
# while i<len(l):
#     d=len(l[i])
#     e=len(l[i])
#     if d<e:
#         e=d
#     if l[i]<min:
#         min=l[i]
#     i=i+1
# l=min,e
# print(l)

# a="this is rama"
# i=0
# while i<len(a):
#     if a[i]==" ":
#         print()
#     else:
#         print(a[i],end="")
#     i=i+1
# b=list(a)
# i=0
# while i<len(b):
#     print(b[i])
#     i=i+1