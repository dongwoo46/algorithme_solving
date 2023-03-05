n = int(input()) 
p = 0

while n>=0:
  if n%5 ==0:
    print(p+n//5)
    break
  n-=3
  p +=1
else:
  print(-1)