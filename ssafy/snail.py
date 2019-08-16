def selectionsort(gets):
    howlong = len(gets)
    for i in range(howlong-1):
        minidx = i
        for j in range(i+1,howlong):
            if gets[minidx] > gets[j]:
                minidx = j
        gets[i], gets[minidx] = gets[minidx], gets[i]
    return gets

gets = list(map(int,input().split()))
print(selectionsort(gets))

