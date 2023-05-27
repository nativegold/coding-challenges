def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        c = str(i) 
        answer += str(c) * min(X.count(c), Y.count(c)) 
        
    if answer == '':
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    
    return answer