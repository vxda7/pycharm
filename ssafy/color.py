test_case = int(input())

for case in range(1,test_case+1):
    howmany = int(input())
    table=[]
    for i in range(10):
        table.append([0]*10)
    for many in range(howmany):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                table[i][j]+=color

    count=0
    for i in range(10):
        for j in range(10):
            if table[i][j] == 3:
                count+=1

    print("#{} {}".format(case, count))