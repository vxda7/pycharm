N = int(input())
gets = list(map(int, input().split()))
temp = 0    # temp 가 1이면 증가 0 평탄 -1 감소
count = 0
vally = 0
where = []
for num in range(N):
    if num != N-1:  # 마지막 지점이 아닐 때
        if gets[num + 1] - gets[num] > 0:   # 증가중이면
            if temp == -1:  # 감소중이었다면
                vally += 1  # 골짜기 증가
            temp = 1    # 증가중으로 변경
        elif gets[num + 1] - gets[num] < 0: # 감소중이라면
            if temp == 1:   # 증가중이었다면
                count += 1  # 봉우리 증가
                where.append(num)   # 봉우리 위치 표시
            temp = -1   # 감소중으로 변경
        else:   # 같다면
            temp = 0    # 평탄

# 봉우리 위치로 가장 긴 다리 찾기
most_long = 0
for i in range(len(where)):
    if i != len(where)-1:
        if where[i+1] - where[i] > most_long:
            most_long = where[i+1] - where[i]


print(count)    # 봉오리
print(vally)    # 골짜기
print(most_long)    # 가장 긴 다리 길이