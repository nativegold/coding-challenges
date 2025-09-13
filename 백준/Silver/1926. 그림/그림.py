import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

stack = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * m for _ in range(n)]
drawing_count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or visited[i][j] == 1:
            continue

        drawing_count += 1
        area = 0
        stack.append((i, j))

        while stack:
            y, x = stack.pop()

            if board[y][x] == 0 or visited[y][x] == 1:
                continue

            visited[y][x] = 1
            area += 1

            for dy, dx in directions:
                next_y = y + dy
                next_x = x + dx

                if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                    continue

                stack.append((next_y, next_x))

        max_area = max(max_area, area)

print(f"{drawing_count}\n{max_area}")