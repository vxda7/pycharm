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

# 선택하기
def find(d, w, k, chosen, films):
    # 정답이 나온경우
    if check(d, w, k):
        return chosen
    temp = films[chosen][:]
    # 첫번째에 A약품을 넣을 경우
    films[chosen] = [0] * w
    if check(d, w, k):
        return chosen
    find(d, w, k, chosen + 1, films)
    films[chosen] = temp[:]
    # chosen번째에 B약품을 넣을 경우
    films[chosen] = [1] * w
    if check(d, w, k):
        return chosen
    find(d, w, k, chosen + 1, films)
    films[chosen] = temp[:]
    # 첫번째를 선택하지 않는 경우
    find(d, w, k, chosen + 1, films)

# 입력받기
t = int(input())
for tc in range(1, t+1):
    D, W, K = map(int, input().split())
    # 0: A      1: B
    films = [list(map(int, input().split())) for i in range(D)]
    # 최소 몇번의 약품추가가 필요한지 확인
    minlength = 100000
    
    if check(D, W, K):  # 검사
        print("#{} {}".format(tc, 0))
    else:
        count = find(D, W, K, 0, films)
        print("#{} {}".format(tc, count))
