l=[[1, 2,8],
   [2, 4,6]]
i=0
b=[]
while i<len(l):
    j=0
    while j<len(l[i]):
        j=j+1
    i=i+1
    b.append(j)
print(b)

# row=len(l)
# column=len(l[i])
# print(row,column)

# l=[[1, 2],
#    [2, 4],[8,7,6]]
# i=0
# b=[]
# co=0
# while i<len(l):
#     co+=1
#     j=0
#     count=0
#     while j<len(l[i]):
#         count+=1
#         j=j+1
#     i=i+1
# print(co,"rows")
# print(count,"colums")