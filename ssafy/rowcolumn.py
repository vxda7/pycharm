arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

row=[0,0,0]
column=[0,0,0,0]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        row[i]+=arr[i][j]

for j in range(len(arr[0])):
    for i in range(len(arr)):
        column[j] += arr[i][j]

print(row)
print(column)