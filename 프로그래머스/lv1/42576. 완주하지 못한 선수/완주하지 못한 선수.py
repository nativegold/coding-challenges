from collections import Counter

def solution(participant, completion):
    p_count = Counter(participant)
    c_count = Counter(completion)
    
    for name, cnt in p_count.items():
        if c_count[name] != cnt:
            return name
    