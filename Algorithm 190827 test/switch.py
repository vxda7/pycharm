swn = int(input())
switch = list(map(int, input().split()))
studentnum = int(input())
for i in range(studentnum):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(swn):
            if (i+1)%num == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0

    else:
        small = min(num-1,  swn - num)
        cnt = 0
        for i in range(1, small+1):
            if switch[num-1+i] == switch[num-1-i]:
                cnt += 1
            else:
                break
        for j in range(num-1-cnt, num+cnt):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0

while len(switch) > 20:
    print(*switch[:20])
    del switch[:20]
print(*switch)


