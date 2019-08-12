T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# K=한번 충전으로 이동할 수 있는 정류장 수 N=정류장 수 M= 충전기 설치 정류장 수
for test_case in range(1, T + 1):
    K, N, M = map(int,input().split())
    stations = list(map(int,input().split()))
    where = range(1,N+1)
    energy=K
    for i in where:
        energy-=1
        for i in where[i:i+K+1]:
            