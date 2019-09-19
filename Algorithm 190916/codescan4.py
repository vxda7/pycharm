import sys
import time

sys.stdin = open("sample_input (11).txt", "r")
start = time.time()

b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
     '1110', '1111']
pattern = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]


def makebin(line):
    global tens
    global b
    global pattern

    temp = []
    for i in line:
        temp.append(b[int(i, 16)])
    temp = ''.join(temp)

    j = 0
    cnt = [0, 0, 0]  # 1,0,1 패턴
    digi = ['0'] * 8
    d = 0
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
            digi[d] = pattern.index(cnt)
            d += 1
        cnt = [0, 0, 0]
        if d == 8:
            if digi not in tens:
                tens.append(digi)
            d = 0
            digi = ['0'] * 8



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
    codearray = set(input().strip('0') for i in range(N))
    res = 0
    tens = []
    same = []
    for i in codearray:
        makebin(i)
    for j in range(len(tens)):
        digit = code(tens[j])
        if digit:
            res += digit
    print("#{} {}".format(tc, res))

print(time.time() - start)
