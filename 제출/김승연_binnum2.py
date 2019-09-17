t = int(input())
for tc in range(1, t + 1):
    N = float(input())
    this = 0.5
    res = []
    for i in range(13):
        if N == 0:
            break
        if N >= this:
            N -= this
            res.append('1')
            this /= 2
        else:
            res.append('0')
            this /= 2
    else:
        res = 'overflow'
    print('#{} {}'.format(tc, ''.join(res)))
