t = int(input())
for tc in range(1, t+1):
    N, M, K = map(int, input().split())
    line = list(map(int, input().split()))
    x = M
    for i in range(K):
        if x == N:
            line.append(line[x % N - 1]+line[x % N ])
        else:
            line.insert(x % N, line[x % N - 1]+line[x % N ])


        print(line, N, x)
        N += 1
        x += M
        if x > N:
            x = x % N
    print("#{}".format(tc),end=" ")
    print(*reversed(line[:]))