from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    count = 0
    
    while len(priorities) != 0:
        ps = priorities.popleft()
        location -= 1

        if len(priorities) != 0 and ps < max(priorities):
            priorities.append(ps)
            if location == -1:
                location = len(priorities) - 1
        else:
            count += 1
            if location == -1:
                return count