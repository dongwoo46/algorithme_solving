def f(idx, num):
    if idx == 6:   #하나의 부분집합 완성
        print(*result)
        return


    for i in range(num, k):
        if not visited[i]:
            result[idx] = s[i]
            visited[i] = 1
            f(idx+1,i+1)
            visited[i] = False
            
while True:
    list1 = list(map(int,input().split()))
    k = list1[0]
    if k == 0:
        exit()
    s = list1[1:]
    visited = [0] * k
    result = [0] * 6
    f(0,0)
    print()