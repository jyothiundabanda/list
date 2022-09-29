# a=['a','b','c','d']
# b=['b','e','g','c']
# i=0
# d=[]
# while i<len(b):
#     if a[i] not in b:
#         d.append(b[i])
#     i=i+1
# print(d)    

l=[11,12,13,14,15,16,17,18,19]
i=0
b=[]
c=-1
while i<(len(l)/2)-2:
    d=[l[i],l[c]]
    b.append(d)
    i=i+1
    c=c-1
print(b)