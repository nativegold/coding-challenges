def solution(progresses, speeds):
    result = []
    complete_days = []
    
    for i in range(len(progresses)):
        remained = 100 - progresses[i]
        needed_days = remained // speeds[i]
        if remained % speeds[i] > 0:
            needed_days += 1
        
        complete_days.append(needed_days)
    
    
    for day in range(max(complete_days)+1):
        completed = 0
        for i in range(len(complete_days)): 
            if complete_days[i] <= day:
                completed += 1 
            else:
                break
                
        if completed > 0:
            result.append(completed)
            
        complete_days = complete_days[completed:]
          
    return result
        
            