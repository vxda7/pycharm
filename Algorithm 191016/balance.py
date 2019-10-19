t = int(input())
for tc in range(1, t + 1):
    # F = G * m1 * m2 / (d*d)
    N = int(input())
    info = list(map(int, input().split()))
    location = info[:N]
    mass = info[N:]
    res = []
    for start in range(N - 1):  # location[start] : 왼쪽끝, location[start + 1] : 오른쪽 끝
        point = (location[start] + location[start + 1]) / 2  # 추정 위치 첫 좌표
        unit = (location[start + 1] - location[start]) / 2  # 변화 단위
        left = 0
        right = 0
        for i in range(start + 1):  # 왼쪽 힘 구하기 왼쪽 좌표값
            left += mass[i] * mass[start] / (point - location[i]) ** 2
        for j in range(start + 1, N):  # 오른쪽 힘 구하기 우측 좌표값
            right += mass[j] * mass[start] / (location[j] - point) ** 2
        left = round(left, 12)
        right = round(right, 12)
        # print(left, right, point, unit)
        beforeleft = left
        beforeright = right
        while round(left, 11) != round(right, 11):
            unit /= 2
            if left > right:
                point += unit
            elif left < right:
                point -= unit
            left = 0
            right = 0
            for i in range(start + 1):  # 왼쪽 힘 구하기 왼쪽 좌표값
                left += mass[i] * mass[start] / (point - location[i]) ** 2
            for j in range(start + 1, N):  # 오른쪽 힘 구하기 우측 좌표값
                right += mass[j] * mass[start] / (location[j] - point) ** 2
            # print(left, right, point)
            if left == beforeleft and right == beforeright:
                break
            beforeleft = left
            beforeright = right
        res.append(round(point, 10))

    print("#{}".format(tc), end=" ")
    for one in res:
        print("%.10f" % one, end=" ")
    print()
