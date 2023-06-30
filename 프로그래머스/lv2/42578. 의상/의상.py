def solution(clothes):
    result = 1
    clothes_count = {}
    
    for c in clothes:
        if c[1] not in clothes_count:
            clothes_count[c[1]] = 1
        else:
            clothes_count[c[1]] += 1
    
    for cnt in clothes_count.values():
        result *= cnt + 1
        
    return result - 1