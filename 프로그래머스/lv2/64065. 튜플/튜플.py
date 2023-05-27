def solution(s):
    answer = []
    
    s = s[2:-2]
    sets = s.split('},{')
    sets.sort(key=len)
    
    for st in sets:
        values = st.split(',')
        
        for v in values:
            if int(v) not in answer:
                answer.append(int(v))
                
    return answer