n = bin(int(input()))[2:]
ans = 0

for i in range(len(n)):
    if n[i] == '1':
        ans += 3**(len(n)-i-1)
print(ans)