import sys
input = sys.stdin.readline

N = int(input())

point_dict = {f'{n}': n for n in range(2, 10)}
point_dict['A'] = 1
point_dict['T'] = 10
point_dict['J'] = 11
point_dict['Q'] = 12
point_dict['K'] = 13

game_board = []
for _ in range(N):
    game_board.append(input().split())

dp = [[0] * N for _ in range(N)]

dp[N-1][0] = point_dict[game_board[N-1][0][0]]

for y in range(N-1, -1, -1):
    for x in range(N):
        score = point_dict[game_board[y][x][0]]

        if y+1 < N:
            dp[y][x] = max(dp[y][x], score + dp[y + 1][x])

        if x-1 >= 0:
            dp[y][x] = max(dp[y][x], score + dp[y][x-1])

print(dp[0][N-1])
