import sys
sys.stdin = open("input (17).txt", "r")


def flycatch(N, M, space, choose):
    best = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            catch = 0

            if choose == 0:
                for k in range(M**2):
                    if k//M ==0 or k%M == M-1:
                        catch += space[i+k//M][j+k%M]
                if catch > best:
                    best = catch

            if choose == 1:
                for k in range(M**2):
                    if k//M ==M-1 or k%M == 0:
                        catch += space[i+k//M][j+k%M]
                if catch > best:
                    best = catch

            if choose == 2:
                for k in range(M**2):
                    if k//M ==M-1 or k%M == 0 or k//M == 0:
                        catch += space[i+k//M][j+k%M]
                if catch > best:
                    best = catch

            if choose == 3:
                for k in range(M**2):
                    if k//M == M-1 or k%M == 0 or k//M == 0 or k%M == M-1:
                        catch += space[i + k // M][j + k % M]
                if catch > best:
                    best = catch

            if choose == 4:
                for k in range(M ** 2):  # k//M  k%M
                    if (k // M + k % M) % 2 == 1:
                        catch += space[i + k // M][j + k % M]
                if catch > best:
                    best = catch
    return best


test_case = int(input())
print("   N  ㄱ  ㄴ  ㄷ  ㅁ  Mosa")
for case in range(1, test_case + 1):
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for i in range(N)]
    # 0: ㄱ     1: ㄴ     2: ㄷ     3: ㅁ     4: Mosaic
    best_giug = flycatch(N, M, space, 0)
    best_nien = flycatch(N, M, space, 1)
    best_digd = flycatch(N, M, space, 2)
    best_mihm = flycatch(N, M, space, 3)
    best_mosa = flycatch(N, M, space, 4)
    print("#{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(case, best_giug, best_nien, best_digd, best_mihm, best_mosa))

