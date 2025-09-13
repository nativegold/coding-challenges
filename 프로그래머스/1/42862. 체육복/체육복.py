def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    same = list(set(lost) & set(reserve))
    for s in same:
        lost.remove(s)
        reserve.remove(s)
        
    answer += n - len(lost)
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
            answer += 1
        elif r+1 in lost:
            lost.remove(r+1)
            answer += 1
    
    return answer