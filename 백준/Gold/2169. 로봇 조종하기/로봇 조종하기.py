import sys


input = sys.stdin.readline

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 행 누적합
for i in range(1, M):
    dp[0][i] += dp[0][i - 1]

# 나머지 행 처리
for i in range(1, N):
    left = [0] * M
    right = [0] * M

    # 왼쪽 → 오른쪽
    left[0] = dp[i][0] + dp[i - 1][0]
    for j in range(1, M):
        left[j] = dp[i][j] + max(left[j - 1], dp[i - 1][j])

    # 오른쪽 → 왼쪽
    right[M - 1] = dp[i][M - 1] + dp[i - 1][M - 1]
    for j in range(M - 2, -1, -1):
        right[j] = dp[i][j] + max(right[j + 1], dp[i - 1][j])

    # 둘 중 최댓값으로 업데이트
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[N - 1][M - 1])