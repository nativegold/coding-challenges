def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)
    al_set = set('qwertyuiopasdfghjklzxcvbnm')
    
    skipped_al = sorted(list(al_set - skip_set))
    
    for c in s:
        answer += skipped_al[(skipped_al.index(c) + index) % len(skipped_al)]
    
    return answer