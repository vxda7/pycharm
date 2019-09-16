def changeb(num):
    for i in range(len(num)):
        if num[i] == '0':
            num[i] = '1'
            break
    return num


def changet(num):
    for i in range(len(num)):
        if num[i] == '1' or num[i] == '0':
            num[i] = '2'
            break
    return num


def second(n, o):
    a = str(bin(n))[2:]
    diff = 0
    for i in range(len(a)):
        if a[i] != o[i]:
            diff += 1

    if diff > 1:
        return False
    elif diff == 1:
        return n


def third(n, o):
    a = ''
    temp = n
    while n >= 3:
        a = str(n % 3) + a
        n = n // 3
    diff = 0
    print(a, o)
    for i in range(len(a)):
        if a[i] != o[i]:
            diff += 1

    if diff > 1:
        return False
    elif diff == 1:
        return temp


def dbt(n):
    a = 0
    for i in range(len(n) - 1, -1, -1):
        a += int(n[i]) * 2 ** i
    return a


def dtt(n):
    a = 0
    for i in range(len(n) - 1, -1, -1):
        a += int(n[i]) * 3 ** i
    return a


t = int(input())
for tc in range(1, t + 1):
    binary = input()
    trio = input()

    big_binary = changeb(list(binary))
    big_trio = changet(list(trio))
    which = max(dbt(big_binary), dtt(big_trio))
    for i in range(which):
        a = second(i, binary)
        b = third(i, trio)
        if a and b and a == b:
            print("#{} {}".format(tc, a))