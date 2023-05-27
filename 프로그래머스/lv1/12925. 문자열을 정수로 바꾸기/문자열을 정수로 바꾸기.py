def solution(s):
    answer = 0
    
    s_list = list(s)    
    
    if s_list[0] == '+':
        s_list.pop(0)
        answer = int(''.join(s_list))
    elif s_list[0] == '-':
        answer = int(''.join(s_list))
    else:
        answer = int(''.join(s_list))
    
    return answer