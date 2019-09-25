N = int(input())
p = list(map(int, input().split()))

mini = N
for i in range(N - 1, 0, -1):
    if p[i - 1] < p[i]:
        mini = i - 1
        break

if mini == N:
    print(-1)
else:
    j = N - 1
    for j in range(N - 1, -1, -1):
        if p[j] > p[mini]:
            break
    p[j], p[mini] = p[mini], p[j]
    end = N - 1
    while mini < end:
        p[mini + 1], p[end] = p[end], p[mini + 1]
        mini += 1
        end -= 1
    print(*p)