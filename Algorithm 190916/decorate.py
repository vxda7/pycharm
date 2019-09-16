t = int(input())
for tc in range(1, t + 1):
    N, A, B = map(int, input().split())
    minV = 10000000000
    R = int(N ** 0.5)
    C = R
    for i in range(max(A, B)):
        value = A * abs(R - C) + B * (N - R * C)
        if value <= minV:
            minV = value
        C += 1
        if R*C > N:
            R -= 1
    print("#{} {}".format(tc, minV))
