arr = [[0]*4 for i in range(4)]
print(arr)

k = 1
for i in range(3):
    for j in range(4):
        if (i<j):
            arr[i][j] = k
            k = k+1
print(arr)

k=10
for i in range(4):
    for j in range(4):
        if (i>j):
            arr[i][j] = k
            k = k + 10
print(arr)
