import sys

n,m = map(int,input().split())

site = {}
for i in range(n):
    a,b = input().split()
    site[a] = b
ans = [input() for _ in range(m)]
for i in ans:
    print(site[i])