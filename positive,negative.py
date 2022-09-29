l=[1,2,3,-2,-4,5,6,-7]
i=0
p=0
n=0
c=0
e=0
while i<len(l):
    d=l[i]
    if d>0:
        p=p+d
        c=c+1
    else:
        n=n+d
        e=e+1
    i=i+1
average=p/c
average1=p/e
print(average1,"negative no")
print(average,"positive number")

# l=[1,2,3,4,5]
# i=0
# s=0
# while i<len(l):
#     d=l[i]
#     s=s+d
#     i+=1
# print(s)
# average=s/d
# print(average)

# l=[1,2,3,4,5]
# i=0
# s=0
# count=0
# while i<len(l):
#     if l[i]%2==0:
#         s=s+l[i]
#         count+=1
#     i+=1
# average=s/count
# print(average)