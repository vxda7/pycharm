def make(start, last):
    global data
    if start <= last:
        if start*2 <= last:
            if data[start] < data[start*2]:
                data[start], data[start*2] = data[start*2], data[start]
        make(start * 2, last)
        make(start * 2 + 1, last)


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    make(1, N)
    print(data)
