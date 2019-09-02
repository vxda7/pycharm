# result = []
# t = int(input())
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     get = list(map(int, input().split()))
#     tlen = N
#     for j in range(M-1):
#         getlist = list(map(int, input().split()))
#         for i in range(N):
#             if get[i] > getlist[0]:
#                 N += tlen
#                 get = get[:i] + getlist + get[i:]
#                 break
#             elif i == N-1:
#                 N += tlen
#                 get = get + getlist
#     result.append(reversed(get[-10:]))
#
#
# for i in range(t):
#     print("#{}".format(i+1), end=' ')
#     print(*result[i])



# result = []
# t = int(input())
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     get = list(map(int, input().split()))
#     tlen = N
#     for j in range(M-1):
#         getlist = list(map(int, input().split()))
#         best = 0
#         for i in range(N):
#             if max(getlist) > best:
#                 best = max(getlist)
#             elif get[i] > getlist[0]:
#                 N += tlen
#
#                 get = get[:i] + getlist + get[i:]
#
#                 if N > 10:
#                     N = 10
#                     if best < max(get[:-10]):     # 10개를 넘을 수 있음
#                         best = max(get[:-10])
#
#                 get = get[-10:]
#                 print(get)
#                 break
#
#             elif i == N-1:
#                 if N >= 10:
#                     N = 10
#                 get = get + getlist
#                 get = get[-10:]
#                 print(get)
#     result.append(reversed(get))
#
#
# for i in range(t):
#     print("#{}".format(i+1), end=' ')
#     print(*result[i])




class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0

        if iterable:
            for value in iterable:
                self.push(value)

    def push(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

        return self
