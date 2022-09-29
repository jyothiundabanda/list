# a=[95,98,67,45,23,43,12,1]
# print(min(a))
# print(max(a))
# print(len(a))
# print(a.index(45))

l=[50,40,23,70,56,12,5,10,7]
i=0
min=l[i]
max=0
while i<len(l):
    a=l[i]
    if a>max:
        max=a
    
    if a<min:
        min=a
    i=i+1
print(max)
print(min)

# a=[50,40,23,70,56,12,5,10,7]
# index=0
# min=a[index]
# max=0
# secondmax=0
# while index<len(a):
#     num=a[index]
#     if num>max:
#         max=num
#     elif num>secondmax:
#         secondmax=num
#     elif num<min:
#         min=num
#     index=index+1
# # max==secondmax
# print(max,"first maximum")
# print(secondmax,"second maximum")
# print(min,"minimum number")


a="my name is jyoti"
b=a.split()
i=0
while i<len(b):
    if i==0 or i==3:
        print(b[i].capitalize()+"-",end='')
    else:
        print(b[i],"-",end="")
    i=i+1

