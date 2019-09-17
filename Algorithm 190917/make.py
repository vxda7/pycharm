for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


def perm(n, k, m):  # m 개의 숫자들에서 k자리의 순열 n은 현재 위치
    global arr
    if k == n:
        print(arr)
    else:
        for i in range(n, m):
            arr[n], arr[i] = arr[i], arr[n]
            perm(n + 1, k, m)
            arr[n], arr[i] = arr[i], arr[n]

arr = [1, 2, 3, 4, 5, 6]
perm(0, 6, 6)