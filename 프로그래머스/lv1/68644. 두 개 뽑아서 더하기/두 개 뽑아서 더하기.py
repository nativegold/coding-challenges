from itertools import combinations

def solution(numbers):
    answer = []

    for x1, x2 in combinations(numbers, 2):
        answer.append(x1 + x2)
        
    return sorted(list(set(answer)))