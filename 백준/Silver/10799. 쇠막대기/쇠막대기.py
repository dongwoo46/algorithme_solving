iron = input()
stack = []
cnt = 0
  
for i in range(len(iron)):
        if iron[i] == '(':
            stack.append(iron[i])
        elif iron[i] ==')':
            if iron[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            elif iron[i-1] == ')':
                stack.pop()
                cnt +=1    
 
 
    # for bracket in iron:
    #     if bracket == '(':
    #         stack.append(bracket)
    #
    #
    #     elif bracket == ')':
    #         if stack[-1] == '(':
    #             stack.pop()
    #             cnt += len(stack)
    #         elif stack[-1] == ')':
    #             stack.pop()
    #     elif iron[-1]
 
print(cnt)