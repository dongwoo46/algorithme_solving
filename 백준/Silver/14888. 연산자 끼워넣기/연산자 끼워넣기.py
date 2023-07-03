

n = int(input())
numb = list(map(int,input().split()))
operator = list(map(int,input().split()))
visited = [0]*4

result = []

def backtracking(v, a, plus, minus,mult,div):
    if v == n:
        result.append(a)
        return


    if plus:
        backtracking(v+1,a+numb[v],plus-1,minus,mult,div)
    if minus:
        backtracking(v+1,a-numb[v],plus,minus-1,mult,div)
    if mult:
        backtracking(v+1,a*numb[v],plus,minus,mult-1,div)
    if div:
        backtracking(v + 1, int(a/numb[v]), plus,minus,mult,div-1)

backtracking(1,numb[0], operator[0], operator[1],operator[2],operator[3])

print(max(result))
print(min(result))