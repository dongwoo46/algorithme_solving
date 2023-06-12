import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    mbti = list(input().split())
    mn = 1e9
    if n>32:
        print(0)
    else:
        for i in range(n-2):
            for j in range(i+1,n-1):
                for l in range(j+1,n):
                    cnt = 0
                    for k in range(4):
                        if mbti[i][k]!=mbti[j][k]:
                            cnt +=1
                        if mbti[i][k] != mbti[l][k]:
                            cnt += 1
                        if mbti[j][k]!=mbti[l][k]:
                            cnt +=1
                    if cnt<mn:
                        mn = cnt
        print(mn)

