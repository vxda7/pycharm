# N = 30
# K = 10
# cnt = 0
# arr = [i for i in range(1, N+1)]
# for i in range(1, 1 << N):
#     s = 0
#     for j in range(N):  # 0에서 9번 비트까지 검사
#         if i & (1 << j):
#             s += arr[j] # j번이 부분집합에 포함되면..
#             # s += j+1 # 인덱스를 직접 부분집합의 숫자로 활용
#     if s == K:
#         cnt += 1
# print(cnt)

# 재귀
def f(i, N, K, s, r):
    global cnt
    global bit
    global cnt2
    cnt2 += 1
    if s == K:  # 나머지 원소를 하나라도 추가하면 K보다 커지므로
        cnt += 1
        return
    elif i == N:    # 모든 원소를 고려했지만 합이 K가 아닌경우
        return
    elif s > K:
        return
    # if i==N:
    #     if s==K:
    #         cnt += 1
    elif s+r < K:
        return
    else:
        f(i+1, N, K, s, r - (i+1)) # i번이 가리키는 값은 부분집합에 포함하지 않는 경우
        f(i+1, N, K, s + i+1, r - (i+1)) # i번이 가리키는 값을 부분집합의 합에 포함


N = 30  # 1부터 N까지가 집합의 원소
K = 105  # 부분집합의 합
cnt = 0
cnt2= 0
bit = [0] * N
f(0, N, K, 0, (1+N)*N//2)
print(cnt)
print(cnt2)
