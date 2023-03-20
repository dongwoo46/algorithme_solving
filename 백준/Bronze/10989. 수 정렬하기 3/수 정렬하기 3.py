import sys

N = int(input())

counts = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    
    counts[num] = counts[num] + 1
    
for i in range(10001):
    if counts[i] != 0:
        for j in range(counts[i]):
            print(i)