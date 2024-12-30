def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    result = 0
    
    for index, t in enumerate(data):
        i = index + 1
        
        if not (row_begin <= i and i <= row_end):
            continue
        
        s = 0
        
        for value in t:
            s += value % i
            
        result ^= s
    
    return result