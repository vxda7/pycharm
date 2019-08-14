def find(pages, want):
    left = 1
    right = pages
    count = 0
    while True:
        center = int((left+right)/2)
        count += 1
        if want == center:
            return count
        elif want > center:
            left = center
        elif want < center:
            right = center


def which(a, b):
    if a == b:
        return 0
    elif a < b:
        return 'A'
    else:
        return 'B'


test_case = int(input())
for case in range(1, test_case+1):
    P, A, B = map(int, input().split())
    print("#{} {}".format(case, which(find(P, A), find(P, B))))
