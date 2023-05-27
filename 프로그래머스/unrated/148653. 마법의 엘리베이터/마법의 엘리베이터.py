def solution(storey):
    count = 0   # 결과(마법의 돌 개수)
    
    while storey > 0:
        remainder = storey % 10 # 맨 뒷 자리부터 한 자리씩 가져오기
    
        # 올림, 내림을 이용해 버튼을 덜 누를 수 있는 방향으로 계산
        # remainder의 값이 5 일 경우 바로 앞 자리의 수가 5 이상이면 올림
        if remainder > 5 or (remainder == 5 and (storey // 10) % 10 >= 5):  # 올림
            count += 10 - remainder
            storey += 10 - remainder
        else:   # 내림
            count += remainder

        storey //= 10 # 맨 뒷 자리 버리기 

    return count