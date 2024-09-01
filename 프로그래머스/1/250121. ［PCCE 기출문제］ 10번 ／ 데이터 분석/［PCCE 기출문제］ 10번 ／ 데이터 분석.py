def solution(data, ext, val_ext, sort_by):
    
    data_index_dict = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
    
    answer = [d for d in data if d[data_index_dict[ext]] < val_ext]        
    answer.sort(key = lambda x: x[data_index_dict[sort_by]])
    
    return answer