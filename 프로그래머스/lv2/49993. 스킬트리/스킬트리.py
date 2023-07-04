from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        correct = True
        
        sk = deque(list(skill))
        for s in st:
            if s in sk:
                if s == sk[0]:
                    sk.popleft()
                else:
                    correct = False
                    break
        
        answer += 1 if correct == True else 0
        
    return answer