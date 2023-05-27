def solution(book_time):
    record = {}
    
    for t in book_time:
        start_time = int(t[0][0:2]) * 60 + int(t[0][3:5])
        end_time = int(t[1][0:2]) * 60 + int(t[1][3:5]) + 10
        
        for minutes in range(start_time, end_time):
            if record.get(minutes) == None:
                record[minutes] = 1
            else:
                record[minutes] += 1
                
    return max(record.values())