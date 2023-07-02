from collections import Counter

def solution(participant, completion):
    # Counter 객체 뺄셈으로 동일하지 않은 부분 찾기
    answer = Counter(participant) - Counter(completion)
    
    return list(answer.keys())[0]
    