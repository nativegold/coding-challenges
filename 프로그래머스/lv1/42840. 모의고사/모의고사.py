def solution(answers):
    answer = []
    correct_count = [[i, 0] for i in range(1, 4)]
    index = [0] * 3
    way1 = [1, 2, 3, 4, 5]
    way2 = [2, 1, 2, 3, 2, 4, 2, 5]
    way3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for ans in answers:
        if ans == way1[index[0]]:
            correct_count[0][1] += 1
        if ans == way2[index[1]]:
            correct_count[1][1] += 1
        if ans == way3[index[2]]:
            correct_count[2][1] += 1
        
        index[0] += 1
        index[1] += 1
        index[2] += 1
        
        if index[0] == len(way1):
            index[0] = 0
        if index[1] == len(way2):
            index[1] = 0
        if index[2] == len(way3):
            index[2] = 0
    
    correct_count.sort(reverse=True, key=lambda x:x[1])
    max_count = 0
    
    for stu, cnt in correct_count:
        if max_count < cnt:
            max_count = cnt
        
        if max_count == cnt:
            answer.append(stu)
            
    return sorted(answer)
    