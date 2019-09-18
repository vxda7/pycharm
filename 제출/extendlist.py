# result = []
# t = int(input())
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     get = list(map(int, input().split()))
#     tlen = N
#     for j in range(M-1):
#         getlist = list(map(int, input().split()))
#         for i in range(N):
#             if get[i] > getlist[0]:
#                 N += tlen
#                 get = get[:i] + getlist + get[i:]
#                 break
#             elif i == N-1:
#                 N += tlen
#                 get = get + getlist
#     result.append(reversed(get[-10:]))
#
#
# for i in range(t):
#     print("#{}".format(i+1), end=' ')
#     print(*result[i])

result = []
t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    get = list(map(int, input().split()))
    tlen = N
    best = 0
    for j in range(M-1):
        getlist = list(map(int, input().split()))
        for i in range(N):
            if get[i] > getlist[0]:
                N += tlen
                if N >= 10:
                    N = 10
                    if best < max(getlist):     # 10개를 넘을 수 있음
                        best = max(getlist)
                get = get[:i] + getlist + get[i:]
                get = get[-10:]
                break
            elif i == N-1:
                N += tlen
                if N >= 10:
                    N = 10
                get = get + getlist
                get = get[-10:]
    result.append(reversed(get))


for i in range(t):
    print("#{}".format(i+1), end=' ')
    print(*result[i])