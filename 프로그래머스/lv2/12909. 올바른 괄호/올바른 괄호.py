def solution(s):
    answer = True
    
    start = 0
    end = 0
    
    for c in s:
        if start < end:
            return False
        
        if c == '(':
            start += 1
        else:
            end += 1
    
    if start != end:
        return False
    else:
        return True