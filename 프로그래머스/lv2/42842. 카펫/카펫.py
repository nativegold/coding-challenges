def solution(brown, yellow):
    area = brown + yellow
    
    for x in range(1, area):
        if (area / x) % 1 == 0:
            y = area / x
            
            if x >= y and brown == (x + y) * 2 - 4:
                return [x, y]
                