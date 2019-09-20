# def find(N, M):
#     visited = [0] * M * 2
#     queue = [0] * M * 10
#     q = -1
#     r = -1
#     q += 1
#     queue[q] = N
#     cnt = 0  # cnt
#     while q != r:
#         # 디큐
#         r += 1
#         n = queue[r]
#         if n == M:
#             break
#         if 0 < n + 1 < 1000000:
#             if visited[n + 1] == 0:
#                 q += 1
#                 queue[q] = n + 1
#                 visited[n + 1] = 1
#         if 0 < n - 1 < 1000000:
#             if visited[n - 1] == 0:
#                 q += 1
#                 queue[q] = n - 1
#                 visited[n - 1] = 1
#         if 0 < n * 2 < 1000000:
#             if visited[n * 2] == 0:
#                 q += 1
#                 queue[q] = n * 2
#                 visited[n * 2] = 1
#         if 0 < n - 10 < 1000000:
#             if visited[n - 10] == 0:
#                 q += 1
#                 queue[q] = n - 10
#                 visited[n - 10] = 1
#         cnt += 1
#
#     return cnt


# def find(N, M):
#     queue = [N]
#     cnt = [0] * 16 * M
#     while queue != []:
#         n = queue.pop(0)
#         if n == M:
#             break
#         else:
#             if 0 < n + 1 < 1000000:
#                 if cnt[n+1] == 0:
#                     queue.append(n + 1)
#                     cnt[n+1] = cnt[n] + 1
#             if 0 < n - 1 < 1000000:
#                 if cnt[n - 1] == 0:
#                     queue.append(n - 1)
#                     cnt[n - 1] = cnt[n] + 1
#             if 0 < n * 2 < 1000000:
#                 if cnt[n * 2] == 0:
#                     queue.append(n * 2)
#                     cnt[n * 2] = cnt[n] + 1
#             if 0 < n - 10 < 1000000:
#                 if cnt[n - 10] == 0:
#                     queue.append(n - 10)
#                     cnt[n - 10] = cnt[n] + 1
#     return cnt[M]


def find(N, M):
    queue = [0] * 1000001
    f, r = -1, -1
    cnt = [0] * 1000001
    r += 1
    queue[r] = N
    while f != r:
        f += 1
        n = queue[f]
        if n == M:
            return cnt[M]
        else:
            if n < M * 2:
                if 0 < n + 1 < 1000001:
                    if cnt[n+1] == 0:
                        r += 1
                        queue[r] = n + 1
                        cnt[n+1] = cnt[n] + 1
                if 0 < n - 1 < 1000001:
                    if cnt[n - 1] == 0:
                        r += 1
                        queue[r] = n - 1
                        cnt[n - 1] = cnt[n] + 1
                if 0 < n * 2 < 1000001:
                    if cnt[n * 2] == 0:
                        r += 1
                        queue[r] = n * 2
                        cnt[n * 2] = cnt[n] + 1
                if 0 < n - 10 < 1000001:
                    if cnt[n - 10] == 0:
                        r += 1
                        queue[r] = n - 10
                        cnt[n - 10] = cnt[n] + 1


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    res = find(N, M)
    print("#{} {}".format(tc, res))


