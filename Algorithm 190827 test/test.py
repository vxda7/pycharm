# import sys
# sys.stdin = open("input2.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stock = list(map(int, input().split()))
    best = -1001    # 최대값 확인
    diffbest = 0    # 최대 수익값
    diffmin = -1001 # 최소 손해값
    same = True     # 그래프에 평탄이 있는가 확인
    lupper = True   # 그래프가 우하향 이다.
    for i in range(n-1,-1,-1):  # 오른쪽부터 왼쪽으로 확인
        if same:
            if best == stock[i]:   # 평탄하면
                diffmin = 0     # 최소 손해는 0
                same = False    # 같은 값이 존재하면 손해는 없으므로 확인 X
            else:
                if best - stock[i] > diffmin:
                    diffmin = best - stock[i]

        if stock[i] > best:
            best = stock[i]
        if best - stock[i] > diffbest:
            diffbest = best - stock[i]
            lupper = False

    if lupper:  # 왼쪽으로 올라만가는 그래프면
        diffbest = diffmin  # 최소 손해가 최대 수익

    print(f"#{tc} {diffbest}")
