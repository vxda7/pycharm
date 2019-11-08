# 검사하기
def check(d, w, k):
    okline = 0
    for i in range(w):
        series = 1
        before = -1
        for j in range(d):
            if films[j][i] == before:
                series += 1
                if series == k:
                    okline += 1
                    break
            else:
                series = 1
            before = films[j][i]
    if okline == w:
        return True
    else:
        return False


def find(d, w, k):
    # 몇개를 선택할지 조합에서 찾기
    minV = 14
    for possible in possibility[d]:
        # possible 에서 1인 값을 바꿔 줄 값으로 선택
        # 선택되었다면 1을 넣을지 2를 넣을지 조합에서 찾기
        howmany= sum(possible)
        tempfilms = films[:]
        zerolist = [0] * w
        onelist = [1] * w

        # 1넣을 가능성, 2넣을 가능성
        for which in possibility[howmany]:
            for one in range(len(which)):
                # A선택
                if which[one] == 0:
                    tempfilms[possible.index(1, one)] = zerolist
                # B선택
                else:
                    tempfilms[possible.index(1, one)] = onelist
                print(possible, which, howmany)
                print(tempfilms)
            if check(d, w, k):
                if minV > howmany:
                    minV = howmany
    return minV


import time
start = time.time()

# 조합 미리 만들어두기
possibility = []
# 0 에 3개  9에 13개에 대한 조합이 저장되어있음
for l in range(13):
    onepossibility = []
    for i in range(1 << l):
        temp = []
        for j in range(l):
            if i & 1 << j:
                temp.append(1)
            else:
                temp.append(0)
        onepossibility.append(temp[:])
    possibility.append(onepossibility[:])
for l in range(10):
    possibility[l].pop(0)

# 입력받기
t = int(input())
for tc in range(1, t + 1):
    D, W, K = map(int, input().split())
    # 0: A      1: B
    films = [list(map(int, input().split())) for i in range(D)]
    # 최소 몇번의 약품추가가 필요한지 확인
    minlength = 100000

    if check(D, W, K):  # 검사
        print("#{} {}".format(tc, 0))
    else:
        count = find(D, W, K)
        print("#{} {}".format(tc, count))
