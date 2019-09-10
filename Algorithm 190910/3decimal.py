def finddecimal():
    res = list(range(2,1000))
    for i in range(2,1000):
        if isdecimal(i):
            res.append(i)
        else:

    return res



t = int(input())
for tc in range(1, t+1):
    N = int(input())    # 7<=N<=999
    decimal = finddecimal()
