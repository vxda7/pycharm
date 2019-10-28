t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    line = list(map(int, input().split()))
    line = list(reversed(sorted(line)))
    hap = 0
    for i in range(2, N - N%3, 3):
        hap += line[i]
    res = sum(line) - hap
    print("#{} {}".format(tc, res))
