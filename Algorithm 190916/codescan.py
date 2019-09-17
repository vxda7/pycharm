import sys

sys.stdin = open("sample_input (11).txt", "r")


def find(N, M):
    global codearray
    res = set()
    for i in range(N - 1, -1, -1):
        temp = codearray[i].strip('0')
        while '0000' in temp:
            start = 0
            for j in range(len(temp) - 4):
                if temp[j:j + 4] == '0000':
                    if temp[start:j].strip('0') not in codearray:
                        res.add(temp[start:j].strip('0'))
                        temp = temp[j:].strip('0')
                        start += len(temp[start:j])
        temp = temp.strip('0')
        res.add(temp)
    res.discard('')
    return res


def makebin(line):
    global tens
    global same
    temp = []
    b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
         '1110', '1111']
    pattern = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]
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
            if digi not in tens:
                tens.append(digi)
                same.append(temp)
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
    lines = find(N, M)
    lines = list(lines)
    print(lines)

    res = []
    tens = []
    same = []
    for i in range(len(lines)):
        makebin(lines[i])
    print(tens)
    for j in range(len(tens)):
        digit = code(tens[j])
        if digit:
            res.append(digit)
    print("#{} {}".format(tc, sum(res)))
