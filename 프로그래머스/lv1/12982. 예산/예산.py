def solution(d, budget):
    budget_result = 0
    count = 0
    
    d.sort()
    for n in d:
        if budget_result + n <= budget:
            budget_result += n
            count += 1
        else:
            break
    
    return count