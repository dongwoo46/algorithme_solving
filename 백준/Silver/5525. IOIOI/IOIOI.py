import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

p = 'IOI'+(n-1)*'OI'
cnt = 0

end = len(p)-1
for start in range(m-len(p)+1):

    if s[start:end+1] == p:
        cnt+=1
    end +=1

print(cnt)