t = int(input())
for tc in range(1, t+1):
    N, M, L = map(int, input().split()) # N 수열길이  M 필요한 숫자  L 출력인덱스
    res = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        res.insert(idx, num)

    print("#{} {}".format(tc, res[L]))

