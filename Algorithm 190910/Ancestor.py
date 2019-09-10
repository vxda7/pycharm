def find(A):
    # global infos
    global c1, c2
    temp = []
    while True:
        if c1[A] == 1:
            break
        else:
            A = c1[A]
            temp.append(A)
    return temp


def findroot(Alist, Blist):
    for i in Alist:
        if i in Blist:
            return i
    return 1


def findnum(root):
    global p1, p2, it
    a = p1[root]
    b = p2[root]
    if a and b:
        return findnum(a) + findnum(b) + 1
    elif a:
        return findnum(a) + 1
    elif b:
        return findnum(b) + 1
    else:
        return 1


t = int(input())
for tc in range(1, t + 1):
    V, E, A, B = map(int, input().split())
    gets = list(map(int, input().split()))

    c1 = [0] * (V + 1)
    c2 = [0] * (V + 1)
    p1 = [0] * (V + 1)
    p2 = [0] * (V + 1)
    it = []
    for i in range(0, E * 2, 2):
        c1[gets[i+1]] = gets[i]
        c2[gets[i+1]] = gets[i]
        if p1[gets[i]]:
            p2[gets[i]] = gets[i + 1]
        else:
            p1[gets[i]] = gets[i+1]

    Alist = find(A)
    Blist = find(B)
    sameroot = findroot(Alist, Blist)
    allnums = findnum(sameroot)
    print(p1, p2)
    print("#{} {} {}".format(tc, sameroot, allnums))

