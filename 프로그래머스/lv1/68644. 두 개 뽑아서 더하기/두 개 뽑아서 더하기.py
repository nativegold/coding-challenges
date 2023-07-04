from itertools import combinations

def solution(numbers):
    answer = []
    
    comb = combinations(numbers, 2)
    for x1, x2 in comb:
        answer.append(x1 + x2)
        
    return sorted(list(set(answer)))