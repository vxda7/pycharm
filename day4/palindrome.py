# # 어째선지 case 3개만 통과됨
# def rot90(cube):
#     long = len(cube)
#     temp = []
#     for i in range(long):
#         temp.append([0]*long)
#     for i in range(long):
#         for j in range(long):
#             temp[i][j] = cube[j][i]
#     return temp
#
#
# def find(lines, N, M):
#     for i in range(N):
#         for j in range(N-M+1):
#             word = lines[i][j:j+M]
#             if word == word[::-1]:
#                 return word
#
#     # lines = rot90(lines)
#     # for i in range(N):
#     #     for j in range(N-M+1):
#     #         word = lines[i][j:j+M]
#     #         if word == word[::-1]:
#     #             return ''.join(word)
#
#     for i in range(N):
#         for j in range(N-M+1): # 0 ~ 7
#             word = ""
#             for k in range(M):
#                 word += lines[j+k][i]
#             if word == word[::-1]:
#                 return word
#
#
# test_case = int(input())
# for case in range(1, test_case+1):
#     N, M = map(int, input().split())
#     lines = []
#     for i in range(M):
#         lines.append(input())
#
#     result = find(lines, N, M)
#
#     print("#{} {}".format(case, result))





# 정답
test_case = int(input())

for case in range(1, test_case+1):
    N, M = map(int, input().split())
    table = []
    for i in range(N):
        table.append(input())
    result='None'

    for i in range(N):
        for j in range(N-M+1):
            word = ""
            for k in range(M):
                word += table[i][k+j]
            if word == word[::-1]:
                result = word
                break

    for i in range(N):
        for j in range(N-M+1):
            word = ""
            for k in range(M):
                word += table[k+j][i]
            if word == word[::-1]:
                result = word
                break

    print("#{} {}".format(case, result))