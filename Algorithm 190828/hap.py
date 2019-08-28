result = []
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))

    best = nums[0]
    for i in range(n):
        for j in range(i, n):
            hap = sum(nums[i:j+1])
            if best < hap:
                best = hap

    result.append(hap)

for i in range(t):
    print("#{} {}".format(i+1, result[i]))



