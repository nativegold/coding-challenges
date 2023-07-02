from itertools import permutations

def solution(k, dungeons):
    # 최대 던전 수
    answer = 0
    
    # 순열 사용
    for pm in permutations(dungeons, len(dungeons)):
        cnt = 0
        fatique = k
        
        # 경우 탐색
        for need, use in pm:
            if fatique >= need:
                fatique -= use
                cnt += 1
            else:
                break
        
        answer = max(answer, cnt)
    
    return answer