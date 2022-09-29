# n="my name is jyothi"
# a=n.split()
# i=0
# b=[]
# l=""
# while i<len(a):
#     d=a[i]
#     e=d[0].upper()
#     k=d.replace(d[0],e)
#     l=l+k
#     l=l+" "
#     i=i+1
# b.append(l)
# print(b)

# a=[10,11,12,13,14,15,16,17,18,19]
# i=1
# b=[]
# while i<len(a):
#     j=0
#     c=[]
#     while j<len(a):
#         if a[i]+a[j]==30 and a[i]>a[j]:
#             k=a[i]
#             l=a[j]
#             c.append(l)
#             c.append(k)
#             b.append(c)
#         j=j+1
#     i=i+1
# print(b)

l=["R",["A"],["N"],["I"]]
i=0
b=[]
while i<len(l):
    if type (l[i]) is list:
        j=0
        while j<len(l[i]):
            num=l[i][j]
            j=j+1
            b.append(num.lower())
    else:
        n=l[i]
        b.append(n)
    i=i+1
p="".join(b)
print([p])

# a=[6,9]
# i=0
# index=min(a)
# b=[]
# while index<=max(a):
#     d=a[i]
#     if d==index:
#         b.append(d)
#     else:
#         b.append(index)
#     index+=1
# print(b)