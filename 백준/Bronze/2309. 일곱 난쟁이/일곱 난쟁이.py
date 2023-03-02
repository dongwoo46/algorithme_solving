
all_short = []
check = 0
for _ in range(9):
    all_short.append(int(input()))



for i in range(8):
    for j in range(i+1,9):
        if sum(all_short) - all_short[i]-all_short[j] == 100 :
            a = all_short[i]
            b = all_short[j]
            check = 1
            break
    if check:
        break
        
all_short.remove(a)
all_short.remove(b)
all_short.sort()

for i in all_short:
    print(i)

