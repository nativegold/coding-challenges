def solution(num, k):
    i = str(num).find(str(k))
    
    if i >= 0:
        return i + 1
    else:
        return -1
        
        