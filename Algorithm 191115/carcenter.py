# 요구조건 => 특정 접수창구와 정비창구를 사용한 고객번호의 합
t = int(input())
for tc in range(1, t+1):
    # N: 접수창구 수, M: 정비창구 수,K: 고객 수 A: 원하는 접수창고 B: 원하는 정비창고
    N, M, K, A, B = map(int, input().split())
    receptions = map(int, input().split())
    repairs =  map(int, input().split())
    cometimes = map(int, input().split())

    waiting_recept = []
    waiting_repair = []
    complete = 0
    while complete != K:
            






