m,n = list(map(int,input().split()))
target = int(input())
delta = [(1,0),(0,1),(-1,0),(0,-1)]

def is_valid(x,y):
    return 0<=x<n and 0<=y<m

def number(x,y):
    global ans_x
    global ans_y
    direction = 0
    cnt = 1
    if target>n*m:
        return
    if target == 1:
        ans_x , ans_y = x,y
        return
    while cnt<n*m:
        nx = x + delta[direction][0]
        ny = y + delta[direction][1]
        if is_valid(nx,ny) and board[nx][ny] == 0:
            cnt += 1
            x, y = nx, ny
            board[nx][ny] = cnt
            if cnt == target:
                ans_x, ans_y = x, y


        else:
            direction = (direction+1)%4

board = [[0]*m for _ in range(n)]
board[0][0] = 1
ans_x=ans_y=-1
number(0,0)
if ans_x!=-1:
    print(ans_y+1,ans_x+1)
else:
    print(0)
