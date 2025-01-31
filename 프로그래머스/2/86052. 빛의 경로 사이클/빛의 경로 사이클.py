
def solution(grid):
    answer = []
    max_row, max_column = len(grid), len(grid[0])
    
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # 상, 좌, 하, 우
    visited = [[[False] * 4 for _ in range(max_column)] for _ in range(max_row)]
    
    for i in range(max_row):
        for j in range(max_column):
            for k in range(4):
                if not visited[i][j][k]:
                    count = 0
                    current_y, current_x = i, j
                    direction = k
                    
                    while not visited[current_y][current_x][direction]:
                        visited[current_y][current_x][direction] = True
                        count += 1
                        
                        current_y = (current_y + directions[direction][0]) % max_row
                        current_x = (current_x + directions[direction][1]) % max_column
                        
                        if grid[current_y][current_x] == 'R':
                            direction = (direction + 1) % 4
                        elif grid[current_y][current_x] == 'L':
                            direction = (direction - 1) % 4
                        
                    answer.append(count)

    return sorted(answer)
    
            
            
