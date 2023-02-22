
def bfs(v, n):
    visited = [0] *(n+1)
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1


def dfs(v,n):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i,n)

v,e,start = list(map(int,input().split()))
graph = [[] for _ in range(v+1)]
visited = [0] * (v + 1)
for i in range(e):
    n1,n2 = list(map(int,input().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)

for x in graph:
    x.sort()


dfs(start,v)
print()
bfs(start,v)


