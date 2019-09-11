def make(start, end):
    global gets, temp
    for i in range(end - 1):
        print(gets, temp)
        get = gets[i]
        if i * 2 + 2 <= end:
            if temp[i] == 0:
                if gets[i * 2 + 1] < get:
                    temp[i] = gets[i * 2 + 1]
                    gets[i], gets[i * 2 + 1] = gets[i * 2 + 1], gets[i]
                elif gets[i * 2 + 2] < get:
                    temp[i] = gets[i * 2 + 2]
                    gets[i], gets[i * 2 + 2] = gets[i * 2 + 2], gets[i]
        else:
            temp[i] = gets[i]


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    gets = [0] + list(map(int, input().split()))
    temp = [0] * (N + 1)
    make(1, N)
    print(temp)
