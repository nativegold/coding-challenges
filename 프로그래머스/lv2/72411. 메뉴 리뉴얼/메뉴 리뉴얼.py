from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for cnt in course:
        candidates = []
        
        for order in orders:
            for comb in combinations(order, cnt):
                candidates.append(''.join(sorted(comb)))
        
        sorted_candidates = Counter(candidates).most_common()
        
        if sorted_candidates[0][1] < 2:
            break
            
        for menu_name, menu_count in sorted_candidates:
            if menu_count > 1 and menu_count == sorted_candidates[0][1]:
                answer.append(menu_name)
                
    return sorted(answer)