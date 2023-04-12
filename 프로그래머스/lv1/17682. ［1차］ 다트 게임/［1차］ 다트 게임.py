def solution(dartResult):
    answer= 0
    tmp = ''
    result = [0]*4
    cnt = 0
    for i in range(len(dartResult)):
        print(cnt)
        if dartResult[i].isdigit():
            tmp+=dartResult[i]
        elif dartResult[i] == 'S': #S,D,T 나오면 다트한게임이 끝난 것
            result[cnt] = int(tmp)
            tmp = ''
            cnt +=1
        elif dartResult[i] == 'D':
            result[cnt] = int(tmp)**2
            tmp = ''
            cnt+=1
        elif dartResult[i] == 'T':
            result[cnt] = int(tmp)**3
            tmp = ''
            cnt+=1
        elif dartResult[i] == '#':
            result[cnt-1] = result[cnt-1]*(-1)
        elif dartResult[i] == '*':
            if cnt == 1:
                result[0] = result[0]*2
            elif cnt == 2:
                result[0] = result[0]*2
                result[1] = result[1]*2
            elif cnt == 3:
                result[1] = result[1]*2
                result[2] = result[2]*2
    answer = sum(result) 
    return answer


