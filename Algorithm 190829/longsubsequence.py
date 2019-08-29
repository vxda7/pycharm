import sys
sys.stdin = open("input.txt", "r")


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    # print(num_list)
    temp = [1]*N
    for i in range(N):
        best = 0
        for j in range(i):
            if num_list[i] >= num_list[j]:
                if best < temp[j]:
                    best = temp[j]
        temp[i] = best + 1
    # print(temp)
    best = max(temp)
    print("#{} {}".format(tc, best))