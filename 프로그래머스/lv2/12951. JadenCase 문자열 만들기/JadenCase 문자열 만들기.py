def solution(s):
    li = s.split(' ')
    result = ''
    
    for x in li:
        if x == '':
            result += ' '
        else:
            result += x[0].upper() + x[1:].lower() + ' '
    
    return result[:-1]
