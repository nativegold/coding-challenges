def solution(s):
    answer = ''
    li = s.split(' ')
    
    for e in li:
        for i, c in enumerate(e):
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '
    
    answer = answer[:-1]
    
    return answer