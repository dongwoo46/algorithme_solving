import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
lst = data
for i in range(1,n):
    lst[i] = max(lst[i], lst[i]+lst[i-1])

print(max(lst))