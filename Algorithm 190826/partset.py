A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    all = []
    for i in range(1, 1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(A[j])
        all.append(temp)

    result = 0
    for i in range(len(all)):
        if len(all[i]) == N and sum(all[i]) == K:
            result += 1
    print("#{} {}".format(tc, result))