# T = int(input())
# for tc in range(1, T + 1):
#     txt = input()
#     temp = []
#     for t in txt:
#         if t == '(':
#             temp.append('(')
#         elif t == ')':
#             if temp:
#                 temp.pop()
#     if not temp:
#         print(True)
#     else:
#         print(False)
#         print(temp)

# teacher
import sys
sys.stdin = open("input.txt", 'r')


def f(txt):
    s = list()
    for i in range(len(txt)):
        # 여는 괄호면 push()
        if txt[i] == '(':
            s.append(txt[i])
        elif txt[i] == ')':
            if len(s) == 0:
                return 0
            else:
                s.pop()
    if len(s) != 0:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    txt = input()
    print(f(txt))
