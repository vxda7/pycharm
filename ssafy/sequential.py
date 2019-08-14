# def sequence(N, V):
#     for i in range(int(N)):
#         if arr[i] == V:
#             return True
#     return False
#
#
# # 개수 N 키 V
# N, V = input().split()
# arr = input().split()
#
# print(sequence(N, V))

def f(n, v, arr):
    for idx in range(0, n):
       if(arr[idx]==v):
           return idx
    return -1

N, V= map(int, input().split())
arr = list(map(int,input().split()))
r = f(N, V, arr)
print(r)