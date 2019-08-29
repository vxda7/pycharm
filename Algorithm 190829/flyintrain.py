t = int(input())
for tc in range(1, t+1):
    D, A, B, F = map(int, input().split())
    time = D/(A+B)
    res = time*F
    print("#{} {}".format(tc, res))