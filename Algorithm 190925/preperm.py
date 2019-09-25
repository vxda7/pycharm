N = int(input())
p = list(map(int, input().split()))

maxi = -1
for i in range(N - 1, -1, -1):
    if p[i - 1] > p[i]:
        maxi = i - 1
        break
if maxi == -1:
    print(-1)
else:
    for j in range(N - 1, maxi, -1):
        if p[j] < p[maxi]:
            break
    p[j], p[maxi] = p[maxi], p[j]
    # print(p, maxi)
    end = N - 1
    while maxi + 1 < end:
        p[maxi + 1], p[end] = p[end], p[maxi + 1]
        end -= 1
        maxi += 1
    print(*p)

