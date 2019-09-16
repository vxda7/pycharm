# my fly X
import sys
sys.stdin = open("input (17).txt", "r")


test_case = int(input())
for case in range(1, test_case + 1):
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for i in range(N)]
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M):
                catch += space[i+k][j+k]
                catch += space[i+M-1-k][j+k]
            if M%2 == 1:
                middle = M//2
                catch -= space[i+middle][j+middle]
            if catch > best:
                best = catch
    print("#{} {}".format(case, best))