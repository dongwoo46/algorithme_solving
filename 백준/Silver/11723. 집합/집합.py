import sys

input = sys.stdin.readline
s = 0
n = int(input())
for _ in range(n):
    order = input().split()
    if order[0] == "add":
        s = s|(1<<int(order[1]))
        continue
    if order[0] == "remove":
        s = s & ~(1<<int(order[1]))
        continue
    if order[0] == "check":
        if s&(1<<int(order[1])):
            print(1)
        else:
            print(0)
        continue
    if order[0] == "toggle":
        s = s^(1<<int(order[1]))
        continue
    if order[0] == "empty":
        s = 0
        continue
    if order[0] == "all":
        s = (1<<21)-1
        continue