def quicksort(l, r):
    global nums, N, res
    if l < r:
        s = partition(l, r)
        if s == N//2:
            res = nums[s]
            return
        quicksort(l, s-1)
        quicksort(s+1, r)


def partition(p, r):
    global nums
    x = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    nums = list(map(int, input().split()))
    l, r = 0, N-1
    res = 0
    quicksort(l, r)
    if res != 0:
        print("#{} {}".format(tc, res))
    else:
        print("#{} {}".format(tc, nums[N//2]))


# def partition(l, r):
#     global nums
#     p = nums[l]
#     i, j = l, r
#     while i <= j:
#         while nums[i] <= p:
#             i += 1
#         while nums[j] >= p:
#             j -= 1
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#
#     nums[l], nums[j] = nums[j], nums[l]
#     return j


