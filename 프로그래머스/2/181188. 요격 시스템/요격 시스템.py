def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    
    end = -1
    
    for i in range(len(targets)):
        if end <= targets[i][0]:
            end = targets[i][1]
            answer += 1
    
    return answer