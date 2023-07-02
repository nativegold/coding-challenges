def solution(clothes):
    result = 1
    clothes_count = {}
    
    # 의상 종류별 갯수로 딕셔너리 만들기
    for c in clothes:
        if c[1] not in clothes_count:
            clothes_count[c[1]] = 1
        else:
            clothes_count[c[1]] += 1
    
    # 의상 갯수로 경우의 수 구하기(입지 않을 경우 포함)
    for cnt in clothes_count.values():
        result *= cnt + 1
    
    # 의상을 입지 않은 경우 제외하고 결과 반환
    return result - 1