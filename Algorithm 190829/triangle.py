# t = int(input())
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     arrx=[]
#     arry=[]
#     temp = {key:[] for key in range(1,N+1)}
#     for i in range(M):
#         x, y = map(int, input().split())
#         arrx.append(x)
#         arry.append(y)
#         temp[x].append(y)
#         temp[y].append(x)
#
#     cnt = 0
#     print(temp)
#     for i in range(1, N+1):
#         for j in range(len(temp[i])):
#             ij = temp[i][j]
#             for k in range(len(temp[ij])):
#                 if temp[ij][k] == i:
#                     cnt += 1
#     # print(cnt)
#     print("#{} {}".format(tc, (cnt-3)//3))


t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arrx=[]
    arry=[]
    temp = {key:[] for key in range(1,N+1)}
    for i in range(M):
        x, y = map(int, input().split())
        arrx.append(x)
        arry.append(y)
        temp[x].append(y)
        temp[y].append(x)

    cnt = 0
    print(temp)
    print(cnt)
    print("#{} {}".format(tc, (cnt-3)//3))