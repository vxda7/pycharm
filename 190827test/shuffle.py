result = []
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    card = list(map(int, input().split()))

    left = card[:n // 2]
    right = card[n // 2:]
    cnt = 0
    sort = sorted(card)
    resort = reversed(sort)

    # print(left)
    # print(right)
    while True:
        temp = []
        if cnt > 5:
            result.append(-1)
            break
        if card == sort or card == resort:
            result.append(cnt)
            break

        if (left[cnt]+1) in right:
            where = right.index(left[cnt] + 1)


        elif (left[cnt]-1) in right:
            where = right.index(left[cnt] - 1)

        cnt += 1

    print(card, cnt)



# if where != 0:
#     temp += right[:where]
#     del right[:where]
# for i in range(n - where):
#     if i % 2 == 0:
#         temp.append(left[0])
#         del left[0]
#     else:
#         temp.append(right[0])
#         del right[0]
# card = temp[:]

# 6 1 4 7 2 5 8 3
#
#