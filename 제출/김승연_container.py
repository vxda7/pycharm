t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers = list(reversed(sorted(containers)))
    trucks = list(reversed(sorted(trucks)))
    move = 0
    for i in range(M):
        for j in range(N):
            if trucks[i] >= containers[j]:
                move += containers[j]
                del containers[j]
                N -= 1
                break
    print("#{} {}".format(tc, move))
