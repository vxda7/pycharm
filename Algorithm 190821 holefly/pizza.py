import sys
sys.stdin = open("sample_input (6).txt", 'r')


def find(N, M, C):
    fire = C[0:N]
    C[0:N] = [0] * N

    cnt = 0
    queue = []
    for i in range(N):
        queue.append(i)     # 화덕의 인덱스 값
    idx = N + 1
    while True:
        for i in range(N):
            fire[i] = fire[i] // 2      # 화덕 치즈값
            if fire.count(0) == N - 1:
                return queue[fire.index(sum(fire))]
            if fire[i] == 0 and N + cnt < M:
                fire[i] = C[N + cnt]
                queue[i] = idx
                C[N + cnt] = 0
                cnt += 1
                idx += 1


test_case = int(input())
for case in range(1, test_case + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    result = find(N, M, C)
    print("#{} {}".format(case, result))


