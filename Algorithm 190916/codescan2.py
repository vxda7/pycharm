import sys

sys.stdin = open("sample_input (11).txt", "r")


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110',
         '1111']
    a = [input() for _ in range(N)]
    s = [''] * N
    used = [[] * M for _ in range(N)]  # 확인된 암호패턴 영역을 표시

    for i in range(N):  # N개의 16진수 라인
        for j in range(M):
            s[i] += b[int(a[i][j], 16)]  # 2 진수의 문자열 형태로 저장

    total = 0
    for i in range(N):
        j = M * 4 - 1
        cnt = [0] * 3  # 1,0,1 패턴
        while j > 54:
            while j > 54 and s[i][j] == '0':
                j -= 1
            while j >= 0 and s[i][j] == '1':
                j -= 1
                cnt[0] += 1
            while j >= 0 and s[i][j] == '0':
                j -= 1
                cnt[1] += 1
            while j >= 0 and s[i][j] == '1':
                cnt[2] += 1
    print("#{} {}".format(tc, s))
