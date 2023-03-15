import sys
from collections import deque


def bfs(x):
    global t
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if visited[b]:
            return visited[b]
        for dx in [-1,1,x]:
            nx = x + dx
            if 0<=nx<100001 and visited[nx] == 0:
                visited[nx] = visited[x]+1
                q.append(nx)




a,b = map(int,input().split())
t= 1
visited = [0]*(100001)
if a==b:
    print(0)
else:
    print(bfs(a))

