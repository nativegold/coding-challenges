def solution(n, words):
    answer = []
    already = set()
    
    for i, w in enumerate(words):
        start = w[0]
        
        if w in already or (i != 0 and start != end):
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            break
        
        end = w[-1]
        already.add(w)
    
    if answer == []:
        return [0, 0]
    
    return answer