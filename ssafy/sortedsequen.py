def f(n, v, arr):
    for idx in range(0, n):
       if(arr[idx]==v):
           return idx
       elif arr[idx] > v:
           return -1
    return -1

N, V= map(int, input().split())
arr = list(map(int,input().split()))
r = f(N, V, arr.sort())
print(r)