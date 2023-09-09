from collections import deque

def make_correct_parentheses(s):
    if s == '':
        return ''
    
    u = ''
    v = deque(s)
    
    while v:
        u += v.popleft()
        
        if u.count('(') == u.count(')'):
            start_count = 0
            end_count = 0
        
            for c in u:
                if c == '(':
                    start_count += 1
                elif c == ')':
                    end_count += 1
                    
                if start_count == end_count:
                    return u + make_correct_parentheses(''.join(v))
                elif start_count < end_count:
                    return '(' + make_correct_parentheses(''.join(v)) + ')' + \
                            u[1:-1].replace('(','0').replace(')','(').replace('0',')')
                
    
def solution(p):
    return make_correct_parentheses(p)