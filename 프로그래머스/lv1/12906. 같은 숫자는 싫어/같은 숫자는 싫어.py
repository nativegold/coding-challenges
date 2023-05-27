def solution(arr):
    s = -1
    answer = []
    
    for i in arr:
        if s != i:
            s = i
            answer.append(s)
    
    return answer
            