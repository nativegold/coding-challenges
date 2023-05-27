def solution(record):
    answer = []
    nickname = {}
    
    for re in record:
        li_re = re.split(' ')
        
        if li_re[0] == "Enter":
            nickname[li_re[1]] = li_re[2]
        elif li_re[0] == "Change":
            nickname[li_re[1]] = li_re[2]
        
    for re in record:
        li_re = re.split(' ')
        
        if li_re[0] == "Enter":
            answer.append(nickname[li_re[1]] + "님이 들어왔습니다.")
        elif li_re[0] == "Leave":
            answer.append(nickname[li_re[1]] + "님이 나갔습니다.")
    
    return answer