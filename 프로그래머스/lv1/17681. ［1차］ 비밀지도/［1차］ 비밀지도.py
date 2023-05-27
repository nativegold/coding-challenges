def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        temp = format(arr1[i] | arr2[i], 'b').zfill(n)
        
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        
        answer.append(temp)
    
    return answer