t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    print("#{} {} {}".format(tc, M - (N - M), N - M))