def solution(board):
    lined_board = ''.join(board)
    count_difference = lined_board.count('O') - lined_board.count('X')
    
    # 개수 확인
    if count_difference not in [0, 1]:
        return 0
    
    col_board = list(zip(*board))
    o_count = 0 
    x_count = 0
    
    # 상하좌우 틱택토 확인
    for i in range(3):
        if board[i].count('O') == 3 or col_board[i].count('O') == 3:
            o_count += 1
        if board[i].count('X') == 3 or col_board[i].count('X') == 3:
            x_count += 1
    
    # 대각선 틱택토 확인
    for i in range(0, 3, 2):
        if board[0][i] == board[1][1] == board[2][2-i] == 'O':
            o_count += 1
        if board[0][i] == board[1][1] == board[2][2-i] == 'X':
            x_count += 1
    
    if o_count and x_count:
        return 0
    if o_count == 1 and count_difference == 0:
        return 0
    if x_count == 1 and count_difference >= 1:
        return 0
    
    return 1