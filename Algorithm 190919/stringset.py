t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    A = set(input().split())
    B = set(input().split())
    original = len(A) + len(B)
    C = A|B
    other = len(C)
    print("#{} {}".format(tc, original - other))