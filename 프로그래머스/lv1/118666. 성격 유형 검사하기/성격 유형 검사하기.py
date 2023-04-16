def check(visited, x):
    if x == 'R' or x =='T':
        visited[0] = 1
    elif x =='C' or x=='F':
        visited[1] = 1
    elif x =='J' or x == 'M':
        visited[2] = 1
    else:
        visited[3] =1
def solution(survey, choices):
    
    power = {'A':1,'R':1,'T':0,'C':1,'F':0,'J':1,'M':0,'N':0}
    order = {'A':3,'R':0,'T':0,'C':1,'F':1,'J':2,'M':2,'N':3}
    dic_team = {"A":'N','C':'F','J':'M','R':'T','N':'A','F':'C','M':'J','T':'R'}
    lst = ['R','T','C','F','J','M','A','N']
    dic = {x:0 for x in lst}
    a = [1,2,3]
    b = [5,6,7]
    visited = [0]*4
    answer = ''
    print(dic)
    for i in range(len(survey)):
        if choices[i] == 1:
            dic[survey[i][0]] +=3
        elif choices[i] == 2:
            dic[survey[i][0]] +=2
        elif choices[i] == 3:
            dic[survey[i][0]] +=1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            dic[survey[i][1]] +=1
        elif choices[i] == 6:
            dic[survey[i][1]] +=2
        elif choices[i] == 7:
            dic[survey[i][1]] +=3

    for i in ['R','C','J','A']:
        if i == 'R':
            if dic[i] > dic[dic_team[i]]:
                answer+=i
            elif dic[i]<dic[dic_team[i]]:
                answer+=dic_team[i]
            else:
                answer+=i
            continue
        if i == 'C':
            if dic[i] > dic[dic_team[i]]:
                answer+=i
            elif dic[i]<dic[dic_team[i]]:
                answer+=dic_team[i]
            else:
                answer+=i
            continue
        if i == 'J':
            if dic[i] > dic[dic_team[i]]:
                answer+=i
            elif dic[i]<dic[dic_team[i]]:
                answer+=dic_team[i]
            else:
                answer+=i
            continue
        if i == 'A':
            if dic[i] > dic[dic_team[i]]:
                answer+=i
            elif dic[i]<dic[dic_team[i]]:
                answer+=dic_team[i]
            else:
                answer+=i
        

    return answer