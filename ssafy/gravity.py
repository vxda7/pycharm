def howmanybest(gets):
    best=-1
    cnt=0
    for get in gets:
        if best == get:
            cnt+=1
        elif best < get:
            best=get
    return cnt

gets = list(map(int,input().split()))
# print(gets.index(max(gets)))
# print(howmanybest(gets))
print(len(gets)-(gets.index(max(gets))+1)-howmanybest(gets))
