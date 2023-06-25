def solution(s1, s2):
    answer = 0
    
    for c in s1:
        if c in s2:
            answer += 1
            
    return answer