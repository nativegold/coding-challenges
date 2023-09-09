from collections import deque

def make_correct_string(s):
    if s == '':
        return ''
    
    u = ''
    v = deque(s)
    
    while v:
        u += v.popleft()
        
        if u.count('(') == u.count(')'):
            new_str = ''
            start_count = 0
            end_count = 0
        
            for c in u:
                if c == '(':
                    start_count += 1
                    new_str += ')'
                elif c == ')':
                    end_count += 1
                    new_str += '('
                    
                print(new_str)
                    
                if start_count == end_count:
                    return u + make_correct_string(''.join(v))
                elif start_count < end_count:
                    return '(' + make_correct_string(''.join(v)) + ')' + new_str[1:-1] 
                
    
def solution(p):
    return make_correct_string(p)