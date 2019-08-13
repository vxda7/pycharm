# gets = list(map(int,input().split()))
gets = list(input())
# triplet 같은거 3개 run 연속3개
triplet=False
run=False

#카드 갯수 count 정렬
counts = [0]*10
for get in gets:
    counts[int(get)] += 1

#triplet 확인
for i in range(10):
   if counts[i] >= 3:
       print("{0} triplet".format(i))
       counts[i]-=3
       triplet=True

#run 확인
for i in range(8):
    if counts[i] == 1 and counts[i+1] == 1 and counts[i+2] ==1:
        print("{0}{1}{2} run".format(i,i+1,i+2))
        run=True

if triplet and run:
    print("Baby-gin!")

