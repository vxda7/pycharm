def digitduet(duet):
    digit = 0
    cnt = 0
    for i in range(len(duet) - 1, -1, -1):
        digit += int(duet[i]) * 2 ** cnt
        cnt += 1
    return digit


def digittrio(trio):
    digit = 0
    cnt = 0
    for i in range(len(trio) - 1, -1, -1):
        digit += int(trio[i]) * 3 ** cnt
        cnt += 1
    return digit


def makeduet(duet):
    global duetlist
    n = len(duet)
    for i in range(n):
        if duet[i] == '0':
            duet[i] = '1'
            duetlist.append(digitduet(duet[:]))
            duet[i] = '0'
        elif duet[i] == '1':
            duet[i] = '0'
            duetlist.append(digitduet(duet[:]))
            duet[i] = '1'


def maketrio(trio):
    global triolist
    n = len(trio)
    for i in range(n):
        if trio[i] == '0':
            trio[i] = '1'
            triolist.append(digittrio(trio[:]))
            trio[i] = '2'
            triolist.append(digittrio(trio[:]))
            trio[i] = '0'
        elif trio[i] == '1':
            trio[i] = '0'
            triolist.append(digittrio(trio[:]))
            trio[i] = '2'
            triolist.append(digittrio(trio[:]))
            trio[i] = '1'
        elif trio[i] == '2':
            trio[i] = '0'
            triolist.append(digittrio(trio[:]))
            trio[i] = '1'
            triolist.append(digittrio(trio[:]))
            trio[i] = '2'


t = int(input())
for tc in range(1, t + 1):
    duet = list(input())
    trio = list(input())

    duetlist = []
    triolist = []
    makeduet(duet)
    maketrio(trio)
    for i in duetlist:
        if i in triolist:
            print("#{} {}".format(tc, i))
            break
