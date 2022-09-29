# l=['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# i=0
# b=[]
# while i<len(l):
#     j=0
#     s=0
#     while i<len(l[i]):
#         s+=l[j][i]
#         j=j+1
#     b.append(s)
#     i=i+1
# print(b)

a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
d=[]
while i<len(a):
    s=(a[i]+b[i]+c[i])
    d.append(s)
    i=i+1
print(d)
