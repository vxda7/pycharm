numbers = int(input())
arr=[]
for number in range(numbers):
    line = list(map(int, input().split()))
    arr.append(line)

cnt = 0
for i in range(1, numbers-1):
    for j in range(1, numbers-1):
        if arr[i][j + 1] == 0 and arr[i][j - 1] == 0 and arr[i + 1][j] == 0 and arr[i - 1][j] == 0 and arr[i][j] == 1:
            cnt += 1

print(cnt)
