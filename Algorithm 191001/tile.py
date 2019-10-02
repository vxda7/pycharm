import sys
sys.stdin = open("input.txt", "r")


t = int(input())
for tc in range(1, t+1):
    N, A, B = map(int, input().split())
    root = int(N ** 0.5)
    R, C = root, root
    temp = A * abs(R - C) + B * (N - R * C)
    minV = A * abs(R - C) + B * (N - R * C)
    if A * abs(R - C) < B * (N - R * C):
        while A * abs(R - C) < B * (N - R * C):
            R += 1
            if B * (N - R * C) < 0:
                R -= 1
                C += 1
                if B * (N - R * C) < 0:
                    break
            temp = A * abs(R - C) + B * (N - R * C)
            if minV > temp:
                minV = temp
    else:
        while A * abs(R - C) > B * (N - R * C):
            R += 1
            if B * (N - R * C) < 0:
                R -= 1
                C += 1
                if B * (N - R * C) < 0:
                    break
            temp = A * abs(R - C) + B * (N - R * C)
            if minV > temp:
                minV = temp
    # print(temp, minV)
    print("#{} {}".format(tc, minV))
