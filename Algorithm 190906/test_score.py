t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    possible = set()
    for i in range(1 << N):
        this = 0
        for j in range(N):
            if i & (1 << j):
                this += scores[j]
        possible.add(this)



