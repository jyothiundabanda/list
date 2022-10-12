# a=[2,1,7,5,3,8]
# # o/p[3,3,1,9,8,1]
# i=0
# j=1
# b=[]
# while i<len(a):
#     n=str(a[i]+j)
#     if len(n)>0:
#         v=n[0]
#         l=int(v)
#         b.append(l)
#     else:
#         h=int(n)
#         b.append(h)
#     i+=1
#     j+=1
# print(b)
    
# l=[2,2,3,4,5,6,6,3,3,2,1,1,4,4,4,5]
# l2=[]
# i=0
# while i<len(l):
#     count=l.count(l[i])
#     a=l[i],count
#     if list(a) not in l2:
#         l2.append(list(a))
#     i=i+1
# print(l2)


# a=[1,2,7,1,2]
# i=0
# b=[]
# while i<len(a):
#     c=a.count(a[i])
#     if c==1:
#         print(a[i])
#     i=i+1
