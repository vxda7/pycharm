q = [0]*9
front = -1
rear = -1
rear += 1   #enq(1) # 시작점 인큐
q[rear] = 1 #enq(1)
visited[1] = 1  #시작점 방문 표시

while(front != rear):   # 큐가 비어있지 않으면
    front += 1
    t = q[front]    # 디큐
    # t에 인접이고 방문하지 않은 정점이면
    # 주어진 상황에 맞게 완성..
    # t 주변의 모든 i에 대해
        if visited[i] == 0 and t에 i가 인접
            ...#enq(i)
            visited[i] = visited[t] + 1