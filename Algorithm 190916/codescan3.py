import sys

sys.stdin = open("sample_input (11).txt", "r")

def makebin(line):
    global tens
    b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
         '1110', '1111']
    pattern = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]

    temp = []
    for i in range(len(line)):
        temp.append(b[int(line[i], 16)])
    temp = ''.join(temp)
    temp = temp.rstrip('0')
    j = 0
    cnt = [0, 0, 0]  # 1,0,1 패턴
    digi = []
    while j < len(temp):
        while j < len(temp) and temp[j] == '0':
            j += 1
        while j < len(temp) and temp[j] == '1':
            j += 1
            cnt[0] += 1
        while j < len(temp) and temp[j] == '0':
            j += 1
            cnt[1] += 1
        while j < len(temp) and temp[j] == '1':
            j += 1
            cnt[2] += 1

        are = min(cnt)
        cnt = cnt[0] * 100 + cnt[1] * 10 + cnt[2]
        if are:
            cnt = cnt // are
        if cnt in pattern:
            digi.append(pattern.index(cnt))
        cnt = [0, 0, 0]
        if len(digi) == 8:
            tens.append(digi)
            digi = []


def code(digit):
    hap = 0
    for i in range(len(digit)):
        if i % 2 == 0:
            hap += digit[i] * 3
        else:
            hap += digit[i]
    if hap % 10 == 0:
        return sum(digit)


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    codearray = [input() for i in range(N)]
    res = []
    tens = []
    for i in range(N):
        makebin(codearray[i])
    for j in range(len(tens)):
        digit = code(tens[j])
        if digit:
            res.append(digit)
    print("#{} {}".format(tc, sum(res)))
