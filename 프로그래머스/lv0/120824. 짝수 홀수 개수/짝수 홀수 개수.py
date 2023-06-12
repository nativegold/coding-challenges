def solution(num_list):
    answer = [0, 0]
    
    for n in num_list:
        if n % 2 == 1:
            answer[1] += 1
        else:
            answer[0] += 1
            
    return answer