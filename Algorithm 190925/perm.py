def perm(n, k):
    if n == k:
        result.append(exam[:])
    else:
        for i in range(n, k):
            exam[n], exam[i] = exam[i], exam[n]
            perm(n + 1, k)
            exam[n], exam[i] = exam[i], exam[n]


N = int(input())
exam = list(range(1, N+1))
result = []
perm(0, N)
result.sort()
for j in range(len(result)):
    print(*result[j])
