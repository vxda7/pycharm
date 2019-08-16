numbers = int(input())
number_board = []
cnt = 0
for number in range(numbers):
    line = list(map(int, input().split()))
    for one in line:
        if one % 2 == 0:
            cnt += 1

print(cnt)

