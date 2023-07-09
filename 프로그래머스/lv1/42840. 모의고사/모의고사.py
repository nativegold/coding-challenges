def solution(answers):
    result = []
    score = [0] * 3
    index = [0] * 3
    way1 = [1, 2, 3, 4, 5]
    way2 = [2, 1, 2, 3, 2, 4, 2, 5]
    way3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for ans in answers:
        if ans == way1[index[0]]:
            score[0] += 1
        if ans == way2[index[1]]:
            score[1] += 1
        if ans == way3[index[2]]:
            score[2] += 1
        
        index[0] += 1
        index[1] += 1
        index[2] += 1
        
        if index[0] == len(way1):
            index[0] = 0
        if index[1] == len(way2):
            index[1] = 0
        if index[2] == len(way3):
            index[2] = 0
    
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i+1)
            
    return result
    