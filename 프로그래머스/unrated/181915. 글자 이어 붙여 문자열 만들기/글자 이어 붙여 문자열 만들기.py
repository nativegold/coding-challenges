def solution(my_string, index_list):
    new_string = ''
    
    for i in index_list:
        new_string += my_string[i]
    
    return new_string