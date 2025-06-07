def calculate(number, width):
    """
    층과 위치 계산
    층: 0부터 시작
    위치: 층이 0이 아니고 홀수 층일 경우, 박스 위치를 왼쪽부터 변환한 위치 제공
    return (층, 방향, 위치)
    """
    
    floor = number // width
    index = number % width
    
    if index == 0:
        floor -= 1
        index = width
    
    from_left = True
    
    if floor % 2 == 1:
        from_left = False
        
    return (floor, from_left, index)


def solution(n, w, num):
    answer = 0
    
    if w == 1:
        return n - num + 1
    
    
    n_floor, n_from_left, n_index = calculate(n, w)
    
    print(n_floor, n_from_left, n_index)
    num_floor, num_from_left, num_index = calculate(num, w)
    print(num_floor, num_from_left, num_index)
    
    answer = n_floor - num_floor  # 층의 차이로 박스 계산 및 num 박스 1개도 포함
    
    if n_from_left == num_from_left:
        if n_index >= num_index:
            answer += 1
    else:
        if n_index + num_index > w:
            answer += 1
    
    return answer