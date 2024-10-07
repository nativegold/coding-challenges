def solution(video_len, pos, op_start, op_end, commands):
    video_len_seconds = to_seconds(video_len)
    pos_seconds = to_seconds(pos)
    op_start_seconds = to_seconds(op_start)
    op_end_seconds = to_seconds(op_end)
    
    for command in commands:
        if op_start_seconds <= pos_seconds and pos_seconds <= op_end_seconds:
            pos_seconds = op_end_seconds
        
        if command == "next":
            pos_seconds += 10
        elif command == "prev":
            pos_seconds -= 10
        
        if pos_seconds < 0:
            pos_seconds = 0
        elif pos_seconds > video_len_seconds:
            pos_seconds = video_len_seconds
            
    if op_start_seconds <= pos_seconds and pos_seconds <= op_end_seconds:
        pos_seconds = op_end_seconds
        
    result_minutes = str(pos_seconds // 60).zfill(2)
    result_seconds = str(pos_seconds % 60).zfill(2)
    
    return f'{result_minutes}:{result_seconds}'


def to_seconds(time):
    time_split = time.split(':') 
    return int(time_split[0]) * 60 + int(time_split[1])