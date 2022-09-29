# l=[3,5,0,13,0,2]
# i=0
# c=0
# a=[]
# b=[]
# while i<len(l):
#     if l[i]==0:
#         s=l[i]
#         a.append(s)
#         c=c+1
#     else:
#         d=l[i]
#         b.append(d)
#     i=i+1
#     e=b+a
# print(e)
# print([c])

# l=[1,2,3,4,5,6,7,8,9,10]
# i=0
# a=[]
# while i<len(l):
#     s=[l[i],l[i+1]]
#     a.append(s)
#     i=i+2
# print(a)

# l=[2,3,4,5,6,7,8]
# i=0
# a=[]
# while i<len(l):
#     b=l[i]
#     s=b+3
#     a.append(s)
#     i=i+1
# print(a)

# l=[2,3,4,5,6,7,8]
# i=0
# a=[]
# while i<len(l):
#     b=l[i]
#     s=b*3
#     a.append(s)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#     i=i+1
# print(a)


# l=["likkitha","sai","jyothi"]
# i=0
# j=-1
# b=[]
# while i<len(l):
#     c=l[i][j]
#     b.append(c)
#     i=i+1
# print(b)





# l=["tamanna","yamanna"]
# i=0
# b=[]
# s=0
# while i<len(l):
#     d=l[i][s]
#     i=i+1
#     print(d,".",end="")


# l=["tamanna","yamanna"]
# i=0

# while i<len(l)/2:
#     print("[",l[i][i].upper(),".",l[i+1][i],"]")

#     i=i+1


# a=["t","a","m","m","a","n","a"]
# b=[]
# i=0
# c=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         c=c+1
#     i=i+1
# print(c)
# print(b)


# a="man"
# b=5
# print("man,"*(b-1)+a)


# from builtins import int

# l=["likkitha","sai","jyothi","jy"]
# i=0
# j=-1
# b=[]
# c=0
# while i<len(l):
#     if c==2:
#         b.append(l[2][0])
#     if c==i:
#         d=l[i][j]
#         b.append(d)
#     i=i+1
#     c=c+1
# print(b)


# l= [1234, 122, 1984, 19372, 100]
# result = True 
# d = str(l[0])
# for i in l:
#     c = str(i)
#     if d[0] != c[0]:
#         result = False
#         break
#     else:
#         continue
# print(result)

# a=['a','b','c','d']
# b=['b','e','g','c']
# i=0
# d=[]
# while i<len(b):
#     if a[i] not in d:
#         d.append(a[i])
#     if b[i] not in b:
#         d.append(b[i])
#     i=i+1
# print(d)


# l=[1,2,3,4,5,6,7,8]
# i=0
# b=[]
# while i<len(l)-1:
#     c=[l[i],l[i+1]]
#     b.append(c)
#     i=i+2
# print(b)

# a=['a','b','c','d']
# b=['b','e','g','c']
# i=0
# d=[]
# while i<len(b):
#     if a[i] not in b:
#         d.append(b[i])
#     i=i+1
# print(d)                


# l=["hell","dear"]
# a=["hello","sir"]

# a=[5,6,8,7,2,3]
# a.sort()
# print(a)
# a.reverse()
# print(a)





# l=[1,2,3,4,5,6,7,8,9]
# i=0
# b=[]
# while i<len(l):
#     d=[l[i],l[i+1],l[i+2]]
#     # v=d[0][1]
#     b.append(d)
#     i=i+3
# print(b)

# l="level"
# i=-1
# c=0
# while i<len(l):
#     d=l[i]
#     v=l.count(d)

#     c=c+1
#     # i=i+1
# print(v)
# print(c)

# s="level"
# l=list(s)
# b=[]
# count=0
# i=0
# while i<len(s)-3:
#     count=s.count(s[i])
#     a=s[i],count
#     b.append(list(a))
#     i=i+1
# print(b)
# print(count+count)

# l=[11,12,13,14,15,16,17,18,19]
# i=0
# b=[]
# c=-1
# while i<(len(l)/2)-2:
#     d=[l[i],l[c]]
#     b.append(d)
#     i=i+1
#     c=c-1
# print(b)



# l=[1,2,3,4]
# b=[96867]
# l.extend(b)
# print(l)

# l="jyojyo"
# a=list(l)
# i=0
# b=[]
# count=0
# while i<len(l)-3:
#     count=l.count(l[i])
#     v=l[i],count
#     b.append(list(v))
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

# l=[2300,530,30,700,2500,10000]
# a=str(l)
# i=0
# while i<len(a):
#     d=a[i]
#     if d!="0":
#         print(d,end="")
#     i=i+1



# a=[[2,3,4],4,5,6]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     if type (a[i]) is list:
#         j=0
#         c=0
#         while j<len(a[i]):
#             c=c+a[i][j]
#             b.append(a[i][j])
#             j=j+1
#     else:
#         sum=sum+a[i]
#         b.append(a[i])
#     i=i+1  
# print(c+sum)
# print(b)

# a=int(input("no"))
# b=str(a)
# c=b[0:4]
# d=b[4:7]
# e=b[7:11]
# print("("+c+")"+"-"+d+"-"+e)





# l=["l","i","k","i","t","h","a"]
# # a=list(l)
# i=0
# while i<len(l):
#     d=l[i]
#     if i==0:
#         print(l[i].capitalize(),end="")
#     else:
#         a=l[i]
#         print(a,end="")
#     i=i+1
    # if type (l[i]) is list:
#         j=0
#         while j<len(l[i]):
#             num=l[i][j]
#             j=j+1
#             b.append(num.lower())
#     else:
#         n=l[i]
#         b.append(n)
#     i=i+1
# p="".join(b)
# print([p])

# list=["l","i","k","i","t","h","a"]
# # # o/p: "Likitha"
# a=''.join()
# print(a)

# l="my name is likitha"
# a=l.split()
# # o/p:MyNameIsLikitha
# i=0
# b=[]
# n=""
# while i<len(a):
#     d=a[i]
#     v=d[0].upper()
#     c=d.replace(d[0],v)
#     n=n+c
#     i=i+1
# b.append(n)
# print(b)


# a="my name is jyoti"
# b=a.split()
# i=0
# while i<len(b):
#     if i==0:
#         print(b[i].capitalize(),end='')
#     else:
#         print(b[i])
#     i=i+1


# o/p[Lkta2iih13]
# l="likitha123"
# i=0
# b=[]
# c=[]
# while i<len(l):
    # if i%2==0:
#         b.append(l[i])
#     else:
#         c.append(l[i])
#     i=i+1
# a="".join(b+c)
# print(a)

# a="my name is ashwini mathpati"
# o/p my name is matupathi
# i=0
# while i<len(a):
#     if a[i]!="aswini":
#         i=i+1
# print(a[:11],a[19::],end="")

# a="mynameisjyothi"
# i=0
# b=" "
# while i<len(a):
#     if i==" ":
#         b=b+a[i]
#     else:
#         b=b+a[i]
#     i=i+1
# print(b)


l=[1,5,[[6,7]],[[8,9]],10,11,[[1,2,3]]]
# print(l[0])
# print(l[1])
# print(l[2][0])
# print(l[2][1])
# print(l[3][0])
# print(l[3][1])
# print(l[4])
# print(l[5])
# print(l[6][0])
# print(l[6][1])
# print(l[6][2])
# print(l[3][0][1])
# print(l[3][0][0])
# print(l[6][0][1])