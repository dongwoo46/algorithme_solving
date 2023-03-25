import sys
m = int(input())
s = 0b0

for _ in range(m):
  cmd = list(map(str, sys.stdin.readline().split()))
  if len(cmd) == 2:
    n = int(cmd[1])
    cmd = cmd[0]
  else:
    cmd = cmd[0]

  if cmd == "check":
    if s & (1 << n): # s and n
      print(1)
    else: # ~(s and n)
      print(0)
  if cmd == "add":
    s = s | (1 << n) # s or n
  if cmd == "remove":
    s = s & ~(1 << n) # s or ~n
  if cmd == "toggle":
    s = s ^ (1 << n) # s xor n
  if cmd == "all":
    s = (1 << 21) - 1
  if cmd == "empty":
    s = 0b0