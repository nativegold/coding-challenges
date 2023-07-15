from itertools import product

def solution(word):
    # 알파벳
    alpha = ['A', 'E', 'I', 'O', 'U']
    #
    dictionary = []
    
    for i in range(1, 6):
        # 중복 순열로 사전 단어 추가
        for p in product(alpha, repeat=i):
            dictionary.append(''.join(p))
    
    # 단어 정렬
    dictionary.sort()
    
    return dictionary.index(word) + 1