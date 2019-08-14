# def f(n, v, arr):
#     while True:
#         n=n//2
#         if v == arr[n]:
#             return n
#         elif v < arr[n]:
#             arr = arr[:n]
#         elif v > arr[n]:
#             arr = arr[n+1:]

def f(N, key, arr):
    left = 0
    right = N-1
    while(left<=right):
        center = (left+right)//2
        if(key == arr[center]):
            return center
        #작은 구간은 버림
        elif arr[center]<key:
            left = center + 1
        # 큰 구간은 버림
        elif key < arr[center]:
            right = center - 1
    # left > right, 1개만 남은 구간에서도 못 찾으면
    return -1

N, V= map(int, input().split())
arr = list(map(int,input().split()))
r = f(N, V, sorted(arr))
print(r)