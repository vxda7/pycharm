# def make(now, possibility):
#     global nums, N, cnt, cnt2
#     cnt2 += 1
#     if now == 10:
#         cnt += 1
#         return
#     elif now > 10 or possibility == N:
#         return
#     else:
#         make(now + nums[possibility], possibility + 1)
#         make(now, possibility + 1)
#
#
# nums = list(range(1,11))
# N = len(nums)
# cnt = 0
# cnt2 = 0
# make(0, 0)
# print(cnt, cnt2)


def f(n, k, s, m, t):
    global cnt
    global cnt2  # 재귀호출의 횟수
    cnt2 += 1

    if s == m:  # 원하는 값에 도달한 경우
        cnt += 1
        return
    elif n == k:  # 하나의 부분집합이 완성된 경우
        return
    elif s > m:  # 부분집합의 합이 찾는 값보다 커진 경우도 중단
        return
    elif s + t < m:  # 남은 원소를 모두 더해도 찾는 값에 못미치는 경우
        return
    else:  # 고려할 원소가 남아있는 경우
        f(n + 1, k, s + a[n], m, t - a[n])  # 부분집합에 포함시키는 경우
        f(n + 1, k, s, m, t - a[n])  # n번 원소를 부분집합에 포함시키지 않는 경우


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
cnt2 = 0
t = sum(a)
f(0, len(a), 0, 53, t)
print(cnt, cnt2)
