from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    max_count = len(queue1) * 3
    
    if sum1 == sum2:
        return 0
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    count = 0
    
    while sum1 != sum2:
        if sum1 > sum2:
            num = queue1.popleft()
            sum1 -= num
            sum2 += num
            queue2.append(num)
            count += 1
        elif sum1 < sum2:
            num = queue2.popleft()
            sum1 += num
            sum2 -= num
            queue1.append(num)
            count += 1
        
        if count == max_count:
            return -1
        
    return count
        
    
    
    