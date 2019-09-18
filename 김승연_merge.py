import time
start = time.time()

def merge(left, right):
    global cnt
    result = [0]*(len(left) + len(right))
    if left[-1] > right[-1]:
        cnt += 1
    l, r, m = 0, 0, 0
    while len(left) != l or len(right) != r:
        if len(left) != l and len(right) != r:
            if left[l] <= right[r]:
                result[m] = left[l]
                l += 1
                m += 1
            else:
                result[m] = right[r]
                r += 1
                m += 1
        else:
            if len(left) != l:
                result[m] = left[l]
                l += 1
                m += 1
            elif len(right) != r:
                result[m] = right[r]
                r += 1
                m += 1
    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    middle = len(nums) // 2
    left = nums[:middle]
    right = nums [middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    numlist = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(numlist)
    # print(result)
    element = result[N//2]
    print("#{} {} {}".format(tc, element, cnt))

print(time.time() - start)