N = list(map(int, input().split()))

everyone = []
def perm(n, k, m):
    global N
    if n == k:
        everyone.append(N[:])
    else:
        for i in range(n, m):
            N[i], N[n] = N[n], N[i]
            perm(n+1, k, m)
            N[i], N[n] = N[n], N[i]


def check(nums):
    if nums[0] + 2 == nums[1] +1 and nums[2] == nums[1] +1:
        return True
    elif nums[0] == nums[1] and nums[1] == nums[2]:
        return True
    return False


perm(0,6,6)

isit = False
print(everyone)
for i in range(len(everyone)):
    first = everyone[i][:3]
    last = everyone[i][3:]
    if check(first) and check(last):
        isit = True

if isit:
    print("baby-gin!")
else:
    print("아님!")
