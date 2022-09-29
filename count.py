list=[1,2,5,4,5,6,6,8,9,10]
i=0
c=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
        # c=c+1
    i=i+1
print(b)


# list= [1, 2, 2, 5, 8, 4, 4, 8]
# i=0
# # c=0
# b=[]
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#     i=i+1
# print(b)




# l=[2,3,4,5,6,7,8]
# i=0
# a=[]
# while i<len(l):
#     b=l[i]
#     s=b*3
#     a.append(s)
#     i=i+1
# print(a)