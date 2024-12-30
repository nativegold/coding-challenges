def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    s_list = []
    
    for index, t in enumerate(data):
        i = index + 1
        
        if not (row_begin <= i and i <= row_end):
            continue
        
        s = 0
        
        for value in t:
            s += value % i
            
        s_list.append(s)
    
    result = 0
    
    for s in s_list:
        result = result ^ s
    
    return result