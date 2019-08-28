import time
import sys
start = time.time()
sys.stdin = open("s_input.txt","r")



# result = []
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     never = True
#     best = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             answer = nums[i] * nums[j]
#             ok = True
#             partial = list(str(answer))
#             # print(partial)
#             if len(partial) != 1:
#                 for k in range(len(partial)-1):
#                     if int(partial[k]) > int(partial[k+1]):
#                         ok = False
#                         break
#             if best < answer and ok == True:
#                 best = answer
#                 never = False
#     if never:
#         result.append(-1)
#     else:
#         result.append(best)

result = []
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    best = 0
    answer_list = []
    for i in range(n):
        for j in range(i+1, n):
            answer = nums[i] * nums[j]
            answer_list.append(answer)

    answer_list.sort()
    answer_list.reverse()
    # print(answer_list)
    for i in range(len(answer_list)):
        ok = True
        word = str(answer_list[i])
        for k in range(len(word)-1):
            if int(word[k]) > int(word[k+1]):
                ok = False
                break
        if ok:
            best = answer_list[i]
            break

    if i == len(answer_list)-1:
        result.append(-1)
    else:
        result.append(best)



for i in range(t):
    print("#{} {}".format(i+1, result[i]))


print("time :", time.time() - start)
