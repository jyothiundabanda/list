# a="AABACAAADA"
# i=1
# while i<len(a)-1:
#     j=1
#     while j<=1:
#         n=a[i]+a[i+1]
#         print(n)
#         j+=1
#     i=i+2

a=["p","q"]
i=1
b=[]
while i<=5:
    j=0
    while j<len(a):
        c=a[j]+str(i)
        # c=a[j]
        b.append(c)
        j=j+1
    i=i+1
print(b)