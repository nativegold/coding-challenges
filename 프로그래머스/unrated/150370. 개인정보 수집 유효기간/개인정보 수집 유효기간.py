def solution(today, terms, privacies):
    answer = []
    expirations = {}
    
    today_split = today.split('.')
    today_to_days = int(today_split[0]) * 12 * 28 + int(today_split[1]) * 28 + int(today_split[2])
    
    for term in terms:
        expirations[term[0]] = int(term[2:]) * 28
    
    for i, privacy in enumerate(privacies):
        exp = expirations[privacy[-1]]
        
        privacy_split = privacy[0:-2].split('.')
        privacy_to_days = int(privacy_split[0]) * 12 * 28 + int(privacy_split[1]) * 28 + int(privacy_split[2])
        
        if privacy_to_days + exp <= today_to_days:
            answer.append(i+1)
        
    return answer