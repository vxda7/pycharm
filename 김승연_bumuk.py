t = int(input())
for tc in range(1, t+1):
    N, D = map(int, input().split())
    maplist = input().split()

    zeros = 0   # 제로갯수
    need = 0    # 설치갯수
    for i in range(N):
        if maplist[i] == '0':
            zeros += 1
        else:
            zeros = 0

        if zeros >= D:
            need += 1
            zeros = 0

    print("#{} {}".format(tc, need))