import sys

input = sys.stdin.readline

N = int(input())
places = []

for _ in range(N):
    places.append(list(map(int, input().split())))

place_dict = {}
safe_place_set = set()

for i in range(N):
    for j in range(N):
        if places[i][j] not in place_dict:
            place_dict[places[i][j]] = []

        safe_place_set.add((i, j))
        place_dict[places[i][j]].append((i, j))

max_safe_area_count = 1
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
stack = []

for h in range(1, 101):
    if h not in place_dict:
        continue

    for i, j in place_dict[h]:
        places[i][j] = -1
        safe_place_set.remove((i, j))

    safe_area_count = 0
    visited = [[False] * N for _ in range(N)]

    for i, j in safe_place_set:
        if places[i][j] == -1 or visited[i][j] == True:
            continue

        safe_area_count += 1
        stack.append((i, j))

        while stack:
            y, x = stack.pop()

            if places[y][x] == -1 or visited[y][x] == True:
                continue

            visited[y][x] = True

            for dy, dx in directions:
                next_y = y + dy
                next_x = x + dx

                if (next_y < 0 or next_y >= N) or (next_x < 0 or next_x >= N):
                    continue

                stack.append((next_y, next_x))

    max_safe_area_count = max(max_safe_area_count, safe_area_count)

print(max_safe_area_count)