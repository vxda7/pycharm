import sys
sys.stdin = open("sample_input (15).txt","r")

t = int(input())
for tc in range(1, t+1):
    n, x = map(int, input().split())
    ground = []
    for i in range(n):
        ground.append(list(map(int, input().split())))

    num = 0
    for col in range(n):
        before = ground[col][0]
        ready = 0   # 평탄이 x칸 있나?
        ok = True   # 설치 가능성
        setting = 0  # 받침대 설치 위치
        for row in range(n):
            check = before - ground[col][row]
            if check == -1:     # 오르막
                if ready < x:   # 준비된 평탄지 보다 x가 크면 끝
                    ok = False
                    break
                ready = 1
            elif check == 1:    # 내리막
                ready = 1
                if row+x <= n:
                    if list(ground[col][row:row+x]) != [ground[col][row]]*x:
                        ok = False
                        break
                    else:
                        ready -= x
                        # setting = row + x - 1
                else:
                    ok = False
                    break
            elif check == 0:
                ready += 1
            else:
                ok = False
                break
            before = ground[col][row]
        if ok:
            # print(col)
            num += 1

    ground = list(zip(*ground))

    # print(ground)
    for col in range(n):
        before = ground[col][0]
        ready = 0   # 평탄이 x칸 있나?
        ok = True   # 설치 가능성
        setting = 0  # 받침대 설치 위치
        for row in range(n):
            check = before - ground[col][row]
            if check == -1:     # 오르막
                if ready < x:   # 준비된 평탄지 보다 x가 크면 끝
                    ok = False
                    break
                ready = 1
            elif check == 1:    # 내리막
                ready = 1
                if row+x <= n:
                    if list(ground[col][row:row+x]) != [ground[col][row]]*x:
                        ok = False
                        break
                    else:
                        ready -= x
                        # setting = row + x - 1
                else:
                    ok = False
                    break
            elif check == 0:
                ready += 1
            else:
                ok = False
                break
            before = ground[col][row]
        if ok:
            # print(col)
            num += 1

    print("#{} {}".format(tc, num))
