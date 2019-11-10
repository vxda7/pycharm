# board = [[1,2,3], [4,5,6], [7,8,9], [1, 2, 3]]
# board = list(zip(*board))
# print(board)
# change = []
# for one in board:
#     word = ''.join(list(map(str,one))).replace('1', '')
#     word_len = len(word)
#     word = '0' * (len(board) + 1 - word_len) + word
#     change.append(list(map(int, word)))
# print(change)
# change = list(map(list, zip(*change)))
# print(change)
