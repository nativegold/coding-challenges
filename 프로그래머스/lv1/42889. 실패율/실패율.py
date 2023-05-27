def solution(N, stages):
    answer = []
    failed = {}
    
    stages.sort()
    
    for n in range(1, N + 1):
        if n in stages:
            failed[n] = stages.count(n) / len(stages[stages.index(n):])
        else:
            failed[n] = 0
    
    for _ in range(len(failed)):
        max_key = max(failed, key=failed.get)
        answer.append(max_key)
        failed.pop(max_key)
    
    return answer