# import sys
# sys.stdin = open('input.txt', 'r')

# # 최대값 구하기
# numbers = int(input())
# for number in range(numbers):
#     gets = list(map(int,input().split()))
#     print("#{0} {1}".format(number+1, max(gets)))

# # 홀수값만 더하기
# numbers = int(input())
# for number in range(numbers):
#     gets = list(map(int,input().split()))
#     gets = [get for get in gets if get%2]
#     print("#{0} {1}".format(number+1, sum(gets)))

# # 평균값 더하기
# numbers = int(input())
# for number in range(numbers):
#     gets = list(map(int,input().split()))
#     print("#{0} {1}".format(number+1, int(round(sum(gets)/len(gets),0))))

# # 큰놈, 작은놈, 같은놈
# numbers = int(input())
# for number in range(numbers):
#     gets = list(map(int,input().split()))
#     if gets[0] > gets[1]:
#         print("#{0} {1}".format(number+1, '>'))

#     elif gets[0] < gets[1]:
#         print("#{0} {1}".format(number+1, '<'))

#     elif gets[0] == gets[1]:
#         print("#{0} {1}".format(number+1, '='))

# # 중간값 찾기
# numbers = int(input())
# gets = list(map(int,input().split()))
# gets.sort()
# print(gets[int(numbers/2)])

# # 자릿수 더하기
# gets = input()
# hap=0
# for get in gets:
#     hap+=int(get)
# print(hap)

# # 연월일 달력
# gets = int(input())
# calender = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for get in range(gets):
#     number = input()
#     if 1 <= int(number[4:6]) <= 12:
#         if 1 <= int(number[6:]) <= calender[int(number[4:6])-1]:
#             print("#{0} {1}".format(get+1, number[0:4]+'/'+number[4:6]+'/'+number[6:]))
#         else:
#             print("#{0} {1}".format(get+1, -1))
#     else:
#         print("#{0} {1}".format(get + 1, -1))

# # 알파벳을 숫자로 변환
# gets = input()
# for get in gets:
#     if get.isupper():
#         print(ord(get)-ord('A')+1, end=' ')
#     elif get.islower():
#         print(ord(get)-ord('a')+1, end=' ')

# #신문 헤드라인
# gets = input()
# print(gets.upper())


# # 스탬프 찍기
# get = int(input())
# for i in range(get):
#     print("#",end="")

# 서랍의 비밀번호
gets = list(map(int, input().split()))
if gets[0] >= gets[1]:
    print(gets[0]-gets[1]+1)
else:
    print(999-gets[1]+1 + gets[0]+1)