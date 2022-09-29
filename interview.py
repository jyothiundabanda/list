
# a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
# i=0
# b=[]
# while i<3:
#     j=i
#     c=[]
#     while j<len(a):
#         num=a[j]
#         c.append(num)
#         j=j+3
#     i=i+1
#     b.append(c)
# print(b)

# a="my name is jyoti"
# i=0
# while i<len(a):
#     if a[i]==" ":
#         print("-",end="")
#     else:
#         print(a[i],end="")
#     i=i+1



# a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# b=[]
# i=0
# while i<len(a):
#     count=0
#     k=a[i]
#     c=[]
#     j=0
#     while j<len(a):
#         l=a[j]
#         if k==l:
#             count+=1
#         j+=1
#     c.append(k)
#     c.append(count)
#     if c not in b:
    #     b.append(c)
    # i+=1
# print(b)


# a=[6,2,3,8]
# # o/p 4,5,7
# i=0
# while i<len(a):
#     d=a[i]-a[i+1]
#     v=a[i+1]+a[i+2]
#     h=a[i+1]-a[i+2]
#     s=a[i+3]+h
#     print(d,v,s)
#     break


# a=[1,2,3,4]
# # o/p [[2,1],[4,3]]
# i=0
# b=[]
# while i<len(a):
#     d=a[i+1]
#     e=a[i]
#     b.append(d)
#     b.append(e)
#     i=i+2
# print(b)


# a=[1,2,3,4] 
# # # o/p [[0,3],[1,2]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]+a[j]==5 and i<j:
#             b.append([i,j])
#         j=j+1
#     i=i+1
# print(b)

# a="likki"
# b=2.0
# c=2
# d=int(b)
# f=c+d
# e=repr(f)
# print(repr(a+e))
# print(b)


# n=input("no")
# a=["books","students",["books","students","books","students","books"]]
# i=0
# count=0
# co=0
# c=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if a[i][j]==a[0]:
#                 count+=1
#             elif a[i][j]==a[1]:
#                 co+=1
#             j=j+1
#     else:
#         if a[i]==a[0]:
#             count+=1
#         elif a[i]==a[1]:
#             co+=1
#     c+=1
#     i=i+1
# print(count,a[0])
# print(co,a[1])
# print(c,n)


