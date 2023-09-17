def solution(s):
    answer = -1
    lst = []
    
    for i in s:
        if len(lst)!=0 and lst[-1] != i:
            lst.append(i)
            continue
        if len(lst)!=0 and lst[-1] == i:
            lst.pop()
            continue
        if len(lst) == 0:
            lst.append(i)
    
    if len(lst) == 0:
        answer = 1
    else:
        answer = 0
        

    return answer