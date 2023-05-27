def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = [str1[i-2:i] for i in range(2, len(str1)+1) if str1[i-2:i].isalpha()]
    set2 = [str2[i-2:i] for i in range(2, len(str2)+1) if str2[i-2:i].isalpha()]
    
    same = []
    
    for s in set1:
        if s in set2:
            same.append(s)
            set2.remove(s)
    
    add = set1 + set2
    
    same_value = len(same)
    add_value = len(add)
    
    if same_value == 0 and add_value == 0:
        answer = 1 
    else:
        answer = same_value / add_value
        
    return int(answer * 65536)