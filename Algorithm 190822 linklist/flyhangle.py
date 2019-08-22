import sys
sys.stdin = open("input (17).txt", "r")


def giug(N, M, space):
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0

            for k in range(M):
                catch += space[i][j+k]
                catch += space[i+k][j+M-1]
            catch -= space[i][j+M-1]
            if catch > best:
                best = catch
    return best


def nien(N, M, space):
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0

            for k in range(M):
                catch += space[i+k][j]
                catch += space[i+M-1][j+k]
            catch -= space[i+M-1][j]
            if catch > best:
                best = catch
    return best


def digd(N, M, space):
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0

            for k in range(M):
                catch += space[i][j+k]
                catch += space[i+k][j]
                catch += space[i+M-1][j+k]
            catch -= space[i][j]
            catch -= space[i+M-1][j]
            if catch > best:
                best = catch
    return best


def mihm(N, M, space):
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0

            for k in range(M):
                catch += space[i][j+k]
                catch += space[i+k][j+M-1]
                catch += space[i+k][j]
                catch += space[i+M-1][j+k]
            catch -= space[i][j]
            catch -= space[i][j+M-1]
            catch -= space[i+M-1][j]
            catch -= space[i+M-1][j+M-1]
            if catch > best:
                best = catch
    return best


def mosa(N, M, space):
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M**2):   # k//M  k%M
                if (k//M + k%M)%2 == 1:
                    catch += space[i + k//M][j + k%M]
            if catch > best:
                best = catch
    return best



test_case = int(input())
for case in range(1, test_case + 1):
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for i in range(N)]

    best_giug = giug(N, M, space)
    best_nien = nien(N, M, space)
    best_digd = digd(N, M, space)
    best_mihm = mihm(N, M, space)
    best_mosa = mosa(N, M, space)

    print("#{} {} {} {} {} {}".format(case, best_giug, best_nien, best_digd, best_mihm, best_mosa))
