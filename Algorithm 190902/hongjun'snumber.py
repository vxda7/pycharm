def which(a, b):
    if a > b:
        return a, b
    else:
        return b, a


def find(A, B):
    v1, v2 = which(A, B)
    stack1=[]
    stack2=[]
    while True:
        s, r = v1 // v2, v1 % v2
        
        stack1.append(s)
        stack2.append(r)







t = int(input())
for tc in range(1, t+1):
    A, B = map(int, input())
    print("#{} {}".format(tc, find(A, B)))


5, 3
5//3 = 1, 5%3 = 2
3//2 = 1, 3%2 = 1
2//1 = 2, 2//1 = 0