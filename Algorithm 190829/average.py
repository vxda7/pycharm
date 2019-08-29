t = int(input())
for tc in range(1, t+1):
    scores = list(map(int, input().split()))
    hap = 0
    for i in range(len(scores)):
        if scores[i] <= 40:
           hap += 40
        else:
            hap += scores[i]
    print("#{} {}".format(tc, hap//len(scores)))