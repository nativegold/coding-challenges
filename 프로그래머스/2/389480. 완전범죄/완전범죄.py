def solution(info, n, m):
    dp = [[[False] * m for _ in range(n)] for _ in range(len(info) + 1)]
    dp[0][0][0] = True
    
    for i, (info_a, info_b) in enumerate(info):
        for a in range(n):
            for b in range(m):
                if dp[i][a][b]:
                    sum_a = a + info_a 
                    if sum_a < n:
                        dp[i + 1][sum_a][b] = True

                    # B가 훔치는 경우
                    sum_b = b + info_b  # 흔적 누적
                    if sum_b < m:
                        dp[i + 1][a][sum_b] = True

    for a in range(n):
        for b in range(m):
            if dp[len(info)][a][b]:
                return a
    
    return -1