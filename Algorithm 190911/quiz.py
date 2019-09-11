t = int(input())
for tc in range(1, t+1):
    nums, cnt = input().split()
    cnt = int(cnt)
    howlong = len(list(nums))
    nums = list(map(int, list(nums)))
