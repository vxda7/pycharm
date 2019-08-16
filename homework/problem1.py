
N = int(input())
gets = list(map(int, input().split()))
best = 0
temp = 0
for i in range(N):
    if i != N-1:    # i가 끝값인지 확인
        if gets[i+1] - gets[i] > 0:     # 증가량이 0보다 큰지 확인
            temp += 1        # 증가량이면 임시값을 1증가
            if temp > best:  # 임시값 중 가장 큰 값을 저장
                best = temp
        else:
            temp = 0    # 감소거나 같은면 임시값 초기화
print(best+1)   # best는 증가량의 갯수 따라서 1을 더해야 증가하는 값들의 길이가 된다.
