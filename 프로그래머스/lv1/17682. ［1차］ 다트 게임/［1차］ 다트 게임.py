def solution(dartResult):
    answer = 0
    before_score = 0
    current_score = 0
    bonus = {'S': 1, 'D': 2, 'T': 3}
    check_number = False
    
    for c in dartResult:
        if c.isdigit():
            if check_number == True:
                current_score = current_score * 10 + int(c)
            else:
                answer += before_score
                before_score = current_score
                current_score = int(c)
                check_number = True
        elif c in bonus:
            current_score **= bonus[c]
            check_number = False
        elif c == '*':
            before_score *= 2
            current_score *= 2
            check_number = False
        elif c == '#':
            current_score = -current_score
            check_number = False
            
    answer += before_score + current_score
    
    return answer