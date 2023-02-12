import sys

n = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result = 0

# 0으로 도화지 크기의 2차원 배열 생성
paper = [[0 for _ in range(101)] for _ in range(101)] 

# 상화좌우 이동 좌표
move = [[0,-1],[0,1],[-1,0],[1,0]]

# 색종이 부분 좌표에 1을 대입
for i,j in data:
  for a in range(i,i+10):
    for b in range(j,j+10):
      paper[a][b] = 1

for x in range(101):
  for y in range(101):
    # x,y좌표가 1이고 주위 좌표가 0인 곳이 선
    if paper[x][y] == 1:
      for z in range(4):
        moveX = x + move[z][0]
        moveY = y + move[z][1]
        if paper[moveX][moveY]==0: 
          result+= 1
print(result)