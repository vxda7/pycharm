def find(N):
    global board
    


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    board = [[0]*N for i in range(N)]
    res = find(N)
    print("#{} {}".format(tc, res))