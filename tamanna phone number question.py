# a=[(123456789)]
# b=list(a)



# b=int(input("enter the number"))
# c=int(b[0:3])
# d=int(b[3:6])
# e=int(b[6:10])
# if len(b)==10:
#     if c>=0 and c<=999:
#         if d>=0 and d<=10000:
#             if e>=0 and e<=10000:
#                 print("("+str(c)+")"+"-"+str(d)+"-"+str(e))
#             else:
#                 print("nothing1")
#         else:
#             print("nothing2")
#     else:
#         print("nothing3")
# else:
#     print("nothing4")

# a=int(input("no"))
# b=str(a)
# c=b[0:4]
# d=b[4:7]
# e=b[7:11]
# print("("+c+")"+"-"+d+"-"+e)


# l=[4,8,10,2]
# i=0
# b=[]
# while i<len(l)-1:
#     j=0
#     while j<len(l)-1:
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#             b.append(l)
#         j=j+1
#     i=i+1
#     break
# print(b)
        


# l=[1,5,4,6,8]
# for j in range(len(l)-1):
#     for i in range(len(l)-1):
#         if l[i]>l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
# print(l)

# n=int(input("no"))
# i=1
# b=[]
# c=0
# while i<=n:
#     j=0
#     c=0
#     if n[i]%2==0:
#         c=c+1
#         break
#     i=i+1
# if c==2:
#     print(c)

# a=list(range(100,200))
# i=0
# b=[]
# while a[i]<a[-1]:
#     count=0
#     j=1
#     while j<=a[i]:
#         if a[i]%j==0:
#             count+=1
#         j=j+1
#     if count==2:
#         b.append(a[i])
#         b.reverse()
#     a[i]+=1
#     i=i+1
# print(b)

# a=int(input("no"))
# c=int(input("no"))
# b=[]
# for i in range(a,c):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         b.append(i)
# print(b)

# a=[[1,2,1],[4,5,6],[10,3]]
# i=0
# b=[]
# while i<len(a):
#     n=a[i]
#     j=0
#     sum=0
#     while j<len(n):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
#     b.append([sum])
# print(b)

# l="my name is rajitha"
# a=l.split()
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i])   :
#         if a[i][j]==a[i][0]:
#             b.append(a[i][j].upper())
#         else:
#             b.append(a[i][j])
#         j=j+1
#     i=i+1
# f="".join(b)
# print([b])

# l="name is rajitha"
# a=l.split()
# i=0
# b=[]
# while i<len(a):
#     # d=a[i],a[i+1]
#     if a[i][0]==a[i]:
#         b.append(a[i].upper())
#     else:
#         b.append(a[i][0])
        
#     i=i+1
# f="".join(b)
# print([b])

# l=[1,2,3,4,5,6,7]
# i=0
# while i<len(l):
#     d=l[i]
#     i=i+1
#     print(d,end=" ")


    



l=["likkitha","sai","jyothi"]
i=0
j=-1
b=[]
while i<len(l):
    c=l[i][j]
    b.append(c)
    i=i+1
print(b)
