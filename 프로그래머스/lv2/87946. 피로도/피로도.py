from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for pm in permutations(dungeons, len(dungeons)):
        cnt = 0
        fatique = k
        
        for need, use in pm:
            if fatique >= need:
                fatique -= use
                cnt += 1
            else:
                break
        
        answer = max(answer, cnt)
    
    return answer