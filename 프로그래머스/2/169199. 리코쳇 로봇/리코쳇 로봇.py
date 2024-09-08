from collections import deque

def solution(board):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    rows, cols = len(board), len(board[0])
    distances = [[float('inf')] * cols for _ in range(rows)]

    print(distances)
    
    queue = deque()

    target_index = [-1, -1]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                distances[i][j] = 0
                queue.append((i, j, 0))
            elif board[i][j] == 'G':
                target_index[0] = i
                target_index[1] = j

    while queue:
        i_y, i_x, value = queue.popleft()

        for d_y, d_x in directions:
            new_y, new_x = i_y, i_x

            while (0 <= new_y + d_y < rows
                   and 0 <= new_x + d_x < cols
                   and board[new_y + d_y][new_x + d_x] != 'D'):
                new_y = new_y + d_y
                new_x = new_x + d_x

            if distances[new_y][new_x] > value + 1:
                distances[new_y][new_x] = value + 1
                queue.append((new_y, new_x, value + 1))

    return -1 if distances[target_index[0]][target_index[1]] == float('inf') else distances[target_index[0]][target_index[1]]

