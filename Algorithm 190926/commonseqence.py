t = int(input())
for tc in range(1, t+1):
    A, B = input().split()

    stack = []
    for i in range(len(A)):
        if A[i] in B:
            stack.append(A[i])
    k = 0
    cnt = 0
    this = []
    for j in range(len(B)):
        if B[j] == stack[k]:
            cnt += 1
            k += 1
    print("#{} {}".format(tc, cnt))