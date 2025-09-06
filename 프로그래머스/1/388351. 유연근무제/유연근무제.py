def to_minute(time):
    return (time // 100) * 60 + time % 100


def solution(schedules, timelogs, startday):
    answer = 0
    day_max_count = 5
    saturday_idx = (13 - startday) % 7
    sunday_idx = (14 - startday) % 7
    
    for i in range(len(schedules)):
        office_going_hour = to_minute(schedules[i]) + 10
        can_receive_reward = True
        timelog = timelogs[i]
        
        j = 0
        
        while j < 7:
            if j in [saturday_idx, sunday_idx]:
                j += 1
                continue
            
            if office_going_hour < to_minute(timelog[j]):
                can_receive_reward = False
                break
                
            j += 1
        
        if can_receive_reward:
            answer += 1
    
    return answer