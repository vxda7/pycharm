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
                    res.add(temp[start:j].strip('0'))
                    temp = temp[j:].strip('0')
                    start += len(temp[start:j])
        temp = temp.strip('0')
        res.add(temp)
        # print(res)
        res.discard('')

    return res


# def check(line):
#     change = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
#               '0111011': 7, '0110111': 8, '0001011': 9}
#     # hextoint = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
#     #             'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
#     interval = len(list(line)) // 14
#     oneline = []
#     digit = []
#     if interval > 1:
#         for i in range(0, len(line), interval):
#             oneline.append(line[i])
#         line = ''.join(oneline)
#
#     binary = bin(int(line, 16))[2:]
#     # print(binary)
#     binary = binary.strip('0')
#     binlen = len(list(binary))
#     if binlen != 56:
#         binary = '0' * (56 - binlen) + binary
#
#     # print(binary, interval)
#     for j in range(0, 56, 7):
#         temp = binary[j:j + 7]
#         if temp in change:
#             digit.append(change[temp])
#     return digit


def makebin(line):
    global tens
    temp = []
    b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
         '1110', '1111']
    pattern = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]
    for i in range(len(line)):
        temp.append(b[int(line[i], 16)])
    temp = ''.join(temp)
    temp = temp.rstrip('0')
    j = 0
    cnt = 0  # 1,0,1 패턴
    digi = []
    while j < len(temp):
        while j < len(temp) and temp[j] == '0':
            j += 1
        while j < len(temp) and temp[j] == '1':
            j += 1
            cnt += 100
        while j < len(temp) and temp[j] == '0':
            j += 1
            cnt += 10
        while j < len(temp) and temp[j] == '1':
            j += 1
            cnt += 1
        print(cnt)
        digi.append(pattern.index(cnt))
        cnt = 0
        print(digi)
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
    lines = find(N, M)
    # print(lines)
    lines = list(lines)

    res = []
    tens = []
    for i in range(len(lines)):
        # digit = check(lines[i])
        makebin(lines[i])
        for j in range(len(tens)):
            digit = code(tens[j])
            if digit:
                res.append(digit)
    print("#{} {}".format(tc, sum(res)))
