test_case = int(input())
for case in range(1, test_case + 1):
    N = int(input())
    farm=[]
    for line in range(N):
        farm.append(list(map(int,list(input()))))
    
    result = 0
    m = [N//2]
    for i in range(N):
        for j in range(N):
            # print(m)
            if j in m:
                result += farm[i][j]
            elif j in m:
                result += farm[i][j]

        if i <N//2:
            m.insert(0,m[0]-1)
            m.append(m[-1]+1)
        elif N//2 <= i <N-1:
            del m[0]
            del m[-1]

            
    
    print("#{} {}".format(case, result))
            
