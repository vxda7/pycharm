# 검사하기
def check(d, w, k, want):
    okline = 0
    for i in range(w):
        series = 1
        before = -1
        for j in range(d):
            if want[j][i] == before:
                series += 1
                if series == k:
                    okline += 1
                    break
            else:
                series = 1
            before = want[j][i]
    if okline == w:
        return True
    else:
        return False


def find(d, w, k):
    # 몇개를 선택할지 조합에서 찾기
    minV = k
    for possible in possibility[d]:
        # possible 에서 1인 값을 바꿔 줄 값으로 선택
        # 선택되었다면 1을 넣을지 2를 넣을지 조합에서 찾기
        howmany= sum(possible)
        tempfilms = films[:]
        zerolist = [0] * w
        onelist = [1] * w
        where = []
        if howmany < k and howmany < minV:
            for a in range(len(possible)):
                if possible[a] == 1:
                    where.append(a)
            # 1넣을 가능성, 2넣을 가능성
            for which in possibility[howmany]:
                for one in range(len(which)):
                    # A선택
                    if which[one] == 0:
                        tempfilms[where[one]] = zerolist
                    # B선택
                    else:
                        tempfilms[where[one]] = onelist
                # print(possible, which, howmany)
                # print(tempfilms)

                if check(d, w, k, tempfilms):
                    if minV > howmany:
                        minV = howmany

    return minV


import time
start = time.time()

# 조합 미리 만들어두기
possibility = []
# 0 에 3개  9에 13개에 대한 조합이 저장되어있음
for l in range(14):
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

# 입력받기
t = int(input())
for tc in range(1, t + 1):
    D, W, K = map(int, input().split())
    # 0: A      1: B
    films = [list(map(int, input().split())) for i in range(D)]
    # 최소 몇번의 약품추가가 필요한지 확인
    if check(D, W, K, films) or K == 1:  # 검사
        print("#{} {}".format(tc, 0))
    else:
        count = find(D, W, K)
        print("#{} {}".format(tc, count))
