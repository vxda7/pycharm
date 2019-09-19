def check(nums):
    for i in range(8):
        if nums[i] != 0 and nums[i+1] != 0 and nums[i+2] != 0:
            return True
        elif nums[i] >= 3:
            return True
    if nums[8] >=3 or nums[9] >= 3:
        return True
    return False


t = int(input())
for tc in range(1, t + 1):
    orders = list(map(int, input().split()))
    playerA = [0] * 10
    playerB = [0] * 10
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            playerA[orders[i]] += 1
        else:
            playerB[orders[i]] += 1

        if i >= 5:
            if check(playerA):
                winner = 1
                break
            elif check(playerB):
                winner = 2
                break
    print("#{} {}".format(tc, winner))
