t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    votes = [0]*N
    for i in range(M):
        for j in range(N):
            if Bi[i] >= Ai[j]:
                votes[j] += 1
                break
    idx = votes.index(max(votes))
    print("#{} {}".format(tc, idx + 1))