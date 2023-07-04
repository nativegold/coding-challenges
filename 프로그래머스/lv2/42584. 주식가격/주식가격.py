from collections import deque

def solution(prices):
    stack = deque([(0, prices[0])])
    result = [0] * len(prices)
    sec = 0
    
    for i in range(1, len(prices)):
        sec += 1
        
        while stack and stack[-1][1] > prices[i]:
            price_index = stack.pop()[0]
            result[price_index] = sec - price_index
        
        stack.append((i, prices[i]))
    
    while stack:
        price_index = stack.pop()[0]
        result[price_index] = sec - price_index
        
    return result