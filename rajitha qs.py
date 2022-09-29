# a=["rajitha"]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if j!=1 and j!=2 and j<=5:
#             c.append(j)
#         j=j+1
#     i=i+1
# print(c)


# a=["rajitha"]
# i=0
# # c=[]
# while i<len(a):
#     d=a[i]
#     n=[d[0],d[3],d[4],d[5]]
#     # c.append(n)
#     i=i+1
# print(n)

# l=["Anga","Likitha"]
# i=0
# b=[]
# while i<len(l):
#     d=l[i]
#     a=d[::-1]
#     b.append(a)
#     b.reverse()
#     i=i+1
# print(b)

# l=[1,3,5]
# i=0
# b=[]
# while i<len(l)-1:
#     d=l[i-2]
#     b.append(d-1)
#     i=i+1
# print(b)



# l=["Anga","Likitha"]
# l.reverse()
# print(l)
# i=0
# b=[]
# while i<len(l):
#     d=l[i]
#     a=d[::-1]
#     b.append(a)
#     i=i+1
# print(b)

# a=[5,7,8,9,10,11]
# i=0
# while i<len(a)-1:
#     b=a[i],a[i+1]
#     print(b)
#     i=i+2

from builtins import int


# a=int(input("enter the a:"))
# b=int(input("enter the b:"))
# c=0
# while a>0:
#     a=a-1
#     c=c+b
# print(a+c)

# i=1
# while i<4:
#     j=1
#     while j<4:
#         if i==2:
#             print(j+1,end=" ")
#         elif i==3:
#             print(j+2,end=" ")
#         else:
#             print(j,end=" ")
#         j=j+1
#     i=i+1
#     print()

# l=["abc","1221","146","111","xyz"]
# i=0
# b=[]
# s=0
# while i<len(l):
#     n=l[i]
#     r=n[::-1]
#     if l[i]==r:
#         s=s+1
#     i=i+1
# print(s)
        
# l="my name is jyothi"
# a=l.split()
# i=0
# b=[]
# while i<len(a):
#     d=l[i]
#     v=l[::-1]
#     b.append(v)
#     i=i+1
#     break
# print(b)

# l="jyothi"
# i=0
# b=[]
# while i<len(l):
#     d=l[i]*5
#     b.append(d)
#     i=i+1
# print(b)

# l="aabcaaada"
# i=1
# while i<len(l):
#     print(l[i],l[i+1])
#     i=i+2

# a=[4,8,2,6,1,9]
# i=-1
# b=[]
# while i>-len(a):
#     j=0
#     while j<len(a):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         # b.append(a[j])
#         j=j+1
#     i=i+1
# print(a)

