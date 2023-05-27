def solution(m, n, puddles):
    map_way = [[0] * (m+1) for _ in range(n+1)]
    
    for x, y in puddles:
        map_way[y][x] = -1
    
    map_way[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif map_way[i][j] == -1:
                map_way[i][j] = 0
            else:
                map_way[i][j] = map_way[i][j-1] + map_way[i-1][j]

    return map_way[n][m] % 1000000007