T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# K=한번 충전으로 이동할 수 있는 정류장 수 N=정류장 수 M= 충전기 설치 정류장 수
for test_case in range(1, T + 1):
    K, N, M = map(int,input().split())
    stations = list(map(int,input().split()))
    energy=K
    count=0
    where=0

    for i in range(N*2+1):
        if energy == 0:
            if where in stations:
                count+=1
                energy=K
            else:
                for j in range(1,K):
                    if where-j in stations:
                        count+=1
                        energy=K
                        where-=j
                        break
                else:
                    count=0
                    break
        if where==N-1:
            break
        where+=1
        energy-=1

    print("#{0} {1}".format(test_case, count))