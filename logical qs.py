# a=[1,2,3,4]
# i=0
# while i<len(a)-1:
#     if a[i]<a[i+1]:
#         a[i],a[i+1]=a[i+1],a[i]
#     i=i+2
# print(a)

# a="jyothiundabanda"
# i=0
# b=""
# c=""
# while i<len(a):
#     if i%2==0:
#         b=b+a[i]
#     else:
#         c=c+a[i]
#     i=i+1
# print(b,c)

# a="JyoTHi" 
# i=0
# b=[]
# while i<len(a):
#     if a[i]==a[i].upper():
#         b.append(i)
#     i=i+1
# print(b)

# a=[2,1,2]
# b=[1,1]
# # o/p;2
# i=0
# c=[]
# while i<len(a):
#     if a[i] not in b:
#         c.append(a[i])
#     i=i+1
# print(c)

# a=["m","na","i","jyo"]
# b=["y","me","s","thi"]
# i=0
# c=[]
# while i<len(a):
#     d=a[i]+b[i]
#     c.append(d)
#     i=i+1
# print(c)

# a=["hello","take"]
# c=["dear","sir"]
# # o/p;["hellodear","hellosir","take dear"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(c):
#         f=a[i]+c[j]
#         b.append(f)
#         j=j+1
#     i=i+1
# print(b)


# a="jyothi"
# i=0
# b=[]
# while i<len(a):
#     d=a[i]*5
#     b.append(d)
#     i=i+1
# print(b)

# print(b)
# print(b)

# a=[[1],[2],[3],[4],[5],[6],[7],[8]]
# i=0
# b=[]
# while i<len(a):
#     # if type (a[i]) is list:
#     j=0
#     while j<len(a[i]):
#         d=a[i][j]
#         b.append(d)
#         j=j+1
#     # else:
#     #     c=a[i]
#     #     b.append(c)
#     i=i+1  
# print(b)

# a=[55,22,33]
# i=0
# while i<len(a):
#     d=a[i]
#     i=i+1
#     print(d,end=" ")


# a=[[5,4,3],[2,1,0],[7,8]]
# # o/p[12,3,15]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a[i]):
#         s=s+a[i][j]
#         j=j+1
#     b.append(s)
#     i=i+1
# print(b)


# a=[[5,4,3],[2,1,0],[7,8]]
# # [14,13,3]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a[i]):
#         s=s+a[j][i]
#         j=j+1
#     b.append(s)
#     i=i+1
# print(b)


# l=["abc","xyz","aba","1221"]
# i=0
# b=[]
# s=0
# while i<len(l):
#     n=l[i]
#     r=n[::-1]
#     if n==r:
#         s=s+1
#     i=i+1
# print(s)

# a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
# # o/p[(2,1),(1,2),(2,3),(4,4),(2,5)]
# i=0
# b=[]
# while i<len(a):
#     d=a[i][1]
#     a.sort()
#     i=i+1
# print(a)

# a=[5,3,6,4,8]
# # o/p[5+1,3+2,6+3,4+4,8+5],[6,5,9,8,13],[6,5,9,8,3]
# i=0
# j=1
# b=[]
# while i<len(a):
#     n=str(a[i]+j)
#     if len(n)>1:
#         s=a[1]
#         k=int(s)
#         b.append(k)
#     else:
#         l=int(n)
#         b.append(l)
#     i+=1
#     j+=1
# print(b)

# l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# # Reverse each list in the said list of lists:
# # [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]
# i=0
# b=[]
# while i<len(l):
#     d=l[i]
#     v=d[::-1]
#     b.append(v)
#     i=i+1
# print(b)



# a=[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
# # Consecutive duplicate elements and their frequency:
# # ([1, 2, 4, 5], [1, 3, 3, 4])
# i=0
# b=[]
# e=[]
# f=[]
# while i<len(a):
#     c=a.count(a[i])
#     if a[i] not in b:
#         b.append(a[i])
#         e.append(c)   
#     i=i+1
# f.append(b)
# f.append(e)
# print(f)

a="jyo","mani"
i=0
b=[]
while i>-len(a):
    d=a[i]
    j=-1
    k=""
    while j>=-len(d):
        k+=d[j]
        j=j-1
    i=i-1
    b.append(k)
print(b)