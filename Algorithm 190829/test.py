t = int(input())
for tc in range(1, t+1):
    N = int(input())
    P = [1, 1, 1, 2, 2]
    for i in range(4,100):
        P.append(P[i] + P[i-4])
    print("#{} {}".format(tc, P[N-1]))