t = int(input())
for tc in range(1, t+1):
    one, two = input().split()
    big = max(len(one), len(two))
    small = min(len(one), len(two))
    dp = [[0]*big for i in range(small)]
