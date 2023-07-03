import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
minnum = 1e9

def backtracking(v,idx):
    global minnum
    if v == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += board[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    power2 += board[i][j]

        minnum = min(minnum,abs(power2-power1))
        return


    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(v+1,i+1)
            visited[i] =0

backtracking(0,0)
print(minnum)

