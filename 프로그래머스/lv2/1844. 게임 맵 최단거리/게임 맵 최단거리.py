from collections import deque

def bfs(maps, start_y, start_x):
    queue = deque([(start_y, start_x)])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    y_len = len(maps)
    x_len = len(maps[0])
    
    while queue:
        y, x = queue.popleft()
        if y == y_len - 1 and x == x_len - 1:
            return maps[y][x]
        
        for dy, dx in direction:
            next_y = y + dy
            next_x = x + dx
            
            if next_y < 0 or next_x < 0 or next_y >= y_len or next_x >= x_len \
                or maps[next_y][next_x] == 0 \
                or (maps[next_y][next_x] != 1 and maps[next_y][next_x] <= maps[y][x] + 1):
                continue
                
            maps[next_y][next_x] = maps[y][x] + 1
            queue.append((next_y, next_x))
        
    return -1
            
    
def solution(maps):
    return bfs(maps, 0, 0)