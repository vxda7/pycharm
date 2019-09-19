def check(word):
    ok = 1  # 이름인가?
    end = ['.', '!', '?']
    for i in range(len(word)):
        if not word[i].isupper() and i == 0:    # 첫글자가 대문자가아니면 단어
            if word[-1] in end:
                ok = 3
            else:
                ok = 0
        else:
            if i != 0:
                if not word[i].islower() and i != len(word)-1:
                    ok = 0
                elif i == len(word) - 1:
                    if word[i] in end and ok == 1:
                        ok = 2
                    elif word[i] in end:
                        ok = 3
                    elif not word[i].islower():
                        ok = 0
    return ok


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    cnt = 0
    res = []


    while True:
        gets = input().split()
        # ok = 0: 이름이 아님, 1: 이름임 2: .으로 끝나는 이름임 3: 다음문장
        for i in range(len(gets)):
            temp = check(gets[i])  # 단어의 상태
            if temp == 1:  # 일반적인 이름으로 끝날 때
                cnt += 1
            elif temp == 2:  # 마지막 글자가 . 인 이름일 때
                res.append(cnt + 1)
                cnt = 0
            elif temp == 3:  # 마지막 글자 일 때
                res.append(cnt)
                cnt = 0

        if len(res) == N:
            print("#{}".format(tc), end=" ")
            print(*res)
            break



