import sys
from collections import deque


delta = [(-1,0),(1,0),(0,-1),(0,1)]
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

ans = [[0]*m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(a,b):
    global ans,visited
    q = deque()
    q.append((a,b))
    ans[a][b] = 0
    visited[a][b] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and board[nx][ny]==1:
                visited[nx][ny] = 1
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx,ny))


for i in range(n):
    for j in range(m):
        if board[i][j]==2:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == 1:
            ans[i][j] = -1
for i in ans:
    for j in i:
        print(j, end=' ')
    print()



