# n=int(input("no."))
# a=0
# i=1
# while n>0:
#     r=n%10
#     a=a+(r*i)
#     i=i*2
#     n=n//10
# print(a)




# n=int(input("enter the length....."))
# i=0
# b=[]
# while i<n:
#     x=int(input("enter the element....."))
#     b.append(x)
#     i=i+1
# print(b)

a=['a','b','c','d']
b=['b','e','g','c']
i=0
d=[]
while i<len(b):
    if a[i] not in b:
        d.append(b[i])
    i=i+1
print(d)
