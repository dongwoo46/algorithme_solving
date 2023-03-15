from collections import deque

a,b = map(int,input().split())
q = deque(x for x in range(1,a+1))
res = []
while q:
    for i in range(b-1):
        q.append(q.popleft())
    res.append(q.popleft())



print('<'+str(res)[1:-1]+'>')