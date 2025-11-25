import sys
input = sys.stdin.readline

N = int(input())
houses_map = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
stack = []
results = []
num_complexes = 0

for i in range(N):
    for j in range(N):
        if houses_map[i][j] == 0 or visited[i][j] is True:
            continue

        stack.append((i, j))
        num_complexes += 1
        houses_count = 0

        while stack:
            y, x = stack.pop()

            if houses_map[y][x] == 0 or visited[y][x] is True:
                continue

            visited[y][x] = True
            houses_count += 1

            if y - 1 >= 0:
                stack.append((y - 1, x))
            if y + 1 < N:
                stack.append((y + 1, x))
            if x - 1 >= 0:
                stack.append((y, x - 1))
            if x + 1 < N:
                stack.append((y, x + 1))

        results.append(houses_count)

results.sort()

print(num_complexes)
for result in results:
    print(result)