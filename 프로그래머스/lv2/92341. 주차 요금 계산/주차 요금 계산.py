from math import ceil

def solution(fees, records):
    answer = []
    in_time = {}
    parking_time = {}
    last_minutes = 23 * 60 + 59
    
    for record in records:
        time, number, state = record.split(' ')
        
        minutes = int(time[3:5]) + int(time[0:2]) * 60
        
        if state == 'IN':
            in_time[number] = minutes
        else:
            if number in parking_time:
                parking_time[number] += minutes - in_time[number]
                in_time.pop(number)
            else:
                parking_time[number] = minutes - in_time[number]
                in_time.pop(number)
    
    for number, in_minutes in in_time.items():
        if number in parking_time:
            parking_time[number] += last_minutes - in_minutes
        else:
            parking_time[number] = last_minutes - in_minutes
    
    pt_array = list(parking_time.items())
    pt_array.sort(key=lambda x:x[0])
    
    for number, pt_minutes in pt_array:
        if pt_minutes <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil((pt_minutes - fees[0]) / fees[2]) * fees[3])
            
    return answer