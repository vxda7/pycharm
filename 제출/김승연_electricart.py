def make(n, k):
    global possibility
    global places
    if n == k:
        possibility.append(places[:])
    else:
        for i in range(n, k):
            places[i], places[n] = places[n], places[i]
            make(n+1, k)
            places[i], places[n] = places[n], places[i]


def find():
    global energy
    global possibility
    minV = 100000000000000
    for i in range(len(possibility)):
        one = [0] + possibility[i] + [0]
        used = 0
        for j in range(len(one)-1):
            used += energy[one[j]][one[j+1]]
        if used < minV:
            minV = used
    return minV

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    energy = [list(map(int, input().split())) for i in range(N)]

    places = list(range(1, N))
    possibility = []
    make(0, N-1)
    res = find()
    print("#{} {}".format(tc, res))
