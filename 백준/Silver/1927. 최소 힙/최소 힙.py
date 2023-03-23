import heapq
import sys


n = int(sys.stdin.readline())
h = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(h, x)
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h))


