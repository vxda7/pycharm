# s = input()
# print(s)
# s = input().split()
# print(s)
# s = list(input())
# print(s)

# s = list(input())
#
# for i in range(0, len(s)//2):
#     s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
# for i in range(0, len(s)):
#     print(s[i], end="")
# print()
# print(''.join(s))


# #문자열비교
# s1 = input()
# s2 = input()
#
# if s1 == s2:
#     print(1)
# else:
#     print(0)
#
# what=True
# for i in range(0, len(s1)):
#     if s1[i] == s2[i]:
#         pass
#     else:
#         what=False
# print(what)
#
# def f(s1, s2):
#     i = 0
#     while (i<len(s1) and i <len(s2)):
#         if s1[i] == s2[i]:
#             i = i + 1
#         else:
#             return 0

def atoi(s):    # '123' -> 123
    change = {'1': 1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
    result = 0
    cnt=0
    for i in s[::-1]:
        result += change[i]*10**cnt
        cnt+=1
    return result

s=input()
print(atoi(s))
print(type(atoi(s)))

def atoi(s):
    n = 0
    for i in range(0, len(s)):
        n = n * 10
        n = n + ord(s[i]) - ord['0']
    return n
s = input()
r = atoi(s)
print(r)