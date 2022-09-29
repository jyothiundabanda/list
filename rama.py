# l="coading is function"
# i=0
# a=l.split()
# while i<len(a):
#     print(len(a[-1]))
#     i=i+1
#     break

# l="coading is function"
# i=0
# # a=l.split()
# while i<len(l):
#     print(l[-1])
#     i=i+1
#     break

# l="Rama","Devi"
# i=0
# while i<len(l)-1:
#     print(l[i][i],".",l[i+1][i])
#     i=i+1

# from os import remove




l=[1,3,5]
i=1
b=[]
while i<len(l)+2:
    if i not in l:
        b.append(i)
    i=i+1
print(b)

# l=[1,2,3,4]
# i=0
# b=[]
# s=0
# while i<len(l):
#     s=s+l[i]
#     b.append(s)
#     i=i+1
# # print(s)
# print(b)