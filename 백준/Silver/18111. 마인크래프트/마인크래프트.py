import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
Height = [list(map(int, input().split())) for _ in range(N)]

min_time = float('inf')
solution_height = 0

for target_height in range(257):
    time = 0
    blocks = B

    for i in range(N):
        for j in range(M):
            current = Height[i][j]
            if current > target_height:
                diff = current - target_height
                blocks += diff
                time += diff * 2
            elif current < target_height:
                diff = target_height - current
                blocks -= diff
                time += diff

    if blocks < 0:
        continue

    if time <= min_time:
        min_time = time
        solution_height = target_height

print(min_time, solution_height)