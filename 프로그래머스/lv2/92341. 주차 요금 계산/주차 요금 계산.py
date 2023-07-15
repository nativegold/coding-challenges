from math import ceil

def solution(fees, records):
    answer = []
    # 차량별 출입 시간
    in_time = {}
    # 차량별 누적 주차 시간
    parking_time = {}
    # 23:59
    last_minutes = 23 * 60 + 59
    
    for record in records:
        # 시간, 차량 번호, 상태
        time, number, state = record.split(' ')
        
        # 시간 '분'으로 변환
        minutes = int(time[3:5]) + int(time[0:2]) * 60
        
        if state == 'IN':   # 입차 기록인 경우
            in_time[number] = minutes
        elif state == 'OUT':   # 출차 기록인 경우
            if number in parking_time:
                parking_time[number] += minutes - in_time[number]
            else:
                parking_time[number] = minutes - in_time[number]
            in_time.pop(number)
    
    # 출차된 내역 없는 기록 정리
    for number, in_minutes in in_time.items():
        if number in parking_time:
            parking_time[number] += last_minutes - in_minutes
        else:
            parking_time[number] = last_minutes - in_minutes
    
    # 차량 번호에 따라 정렬
    pt_array = list(parking_time.items())
    pt_array.sort(key=lambda x:x[0])
    
    # 요금 계산
    for number, pt_minutes in pt_array:
        if pt_minutes <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil((pt_minutes - fees[0]) / fees[2]) * fees[3])
            
    return answer