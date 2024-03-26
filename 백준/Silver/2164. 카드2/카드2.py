from collections import deque

n = int(input())
queue = deque([card for card in range(1, n+1)])

current = 0
while queue:
    current = queue.popleft()
    if queue:
        queue.append(queue.popleft())

print(current)
