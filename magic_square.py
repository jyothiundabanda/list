a=[[2,7,6],
  [9,5,1],
  [4,3,8]]
i=0
while i<len(a):
    j=0
    sum_row=0
    while j<len(a[i]):
        sum_row=sum_row+a[i][j]
        j=j+1
    i=i+1
print("row",sum_row)
i=0
while i<len(a):
    j=0
    sum_col=0
    while j<len(a[i]):
        sum_col=sum_col+a[i][j]
        j=j+1
    i=i+1
print("col",sum_col)
    























# a=[[5, 7, 1],
#   [9, 0, 1],
#   [1, 3, 2]]
# i=0
# while i<len(a):
#     j=0
#     sumr=0
#     while j<len(a[i]):
#         sumr=sumr+a[i][j]
#         j+=1
#     i+=1
# print("sumr:",sumr)
# i=0
# while i<len(a):
#     j=0
#     sumc=0
#     while j<len(a[i]):
#         sumc=sumc+a[j][i]
#         j+=1
#     i+=1
# print("sumc:",sumc)
# i=0
# r=2
# m=0
# while i<len(a):
#     j=2
#     while j<len(a):
#         m+=a[i][r]
#         j+=1
#         r-=1
#     i+=1
# print("m:",m)
# # i=0
# # p=0
# # n=0
# # while i<len(a):
# #     j=2
# #     while j<len(a):
# #         n+=a[i][p]
# #         j+=1
# #         p+=1
# #     i+=1
# # print("n:",n)
# print()
# if sumr==sumc==m:
#     print(a,"it is a magic square")
# else:
#     print(a,"it is not a magic square")