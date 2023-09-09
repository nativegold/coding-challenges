from collections import deque

def make_correct_parentheses(s):
    if s == '':  # 빈 문자열인 경우 그대로 반환.
        return ''
    
    u = ''
    v = deque(s)
    
    while v:  # v가 빌 때까지 반복
        u += v.popleft()
        
        # u에 있는 '('와 ')'의 개수가 같아질 때
        if u.count('(') == u.count(')'):
            start_count = 0  # '('의 개수를 저장
            end_count = 0  # ')'의 개수를 저장
        
            # u 안의 문자들을 하나씩 검사
            for c in u:
                if c == '(':
                    start_count += 1  # '('를 발견할 때마다 start_count를 1 증가
                elif c == ')':
                    end_count += 1  # ')'를 발견할 때마다 end_count를 1 증가.
                    
                # '('와 ')'의 개수가 같을 때
                if start_count == end_count:
                    # 현재의 u와 재귀적으로 v를 올바른 괄호 문자열로 만든 값을 더해 반환
                    return u + make_correct_parentheses(''.join(v))
                # ')'의 개수가 더 많을 때
                elif start_count < end_count:
                    # 문제에서 정의한 방법에 따라 문자열을 재배열하고 반환
                    return '(' + make_correct_parentheses(''.join(v)) + ')' + \
                            u[1:-1].replace('(','0').replace(')','(').replace('0',')')

def solution(p):
    return make_correct_parentheses(p)