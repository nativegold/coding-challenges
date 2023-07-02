def solution(brown, yellow):
    # 전체 넓이
    area = brown + yellow
    
    # 카펫의 가로 길이(x), 카펫의 세로 길이(y)
    for x in range(1, area):
        # 가로 길이로 넓이가 나누어질 때
        if (area / x) % 1 == 0:
            y = area / x
            
            if x >= y and brown == (x + y) * 2 - 4:
                return [x, y]
                