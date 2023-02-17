T = int(input())
for tc in range(1,T+1):
    n = int(input())
    route = [0]*200
    for _ in range(n):
        s, e = map(int,input().split())
        if s>e:
            s, e = e,s
            for i in range((s-1)//2,(e-1)//2+1):
                route[i] += 1
        else:
            for i in range((s-1)//2,(e-1)//2+1):
                route[i] += 1
    print(f'#{tc} {max(route)}')