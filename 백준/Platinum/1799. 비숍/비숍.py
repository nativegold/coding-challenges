import sys

input = sys.stdin.readline

n = int(input())    # 체스판 크기
board = [list(map(int, input().split())) for _ in range(n)]  # 체스판
max_bishops = 0  # 놓을 수 있는 최대 비숍 개수 저장 변수

# 우상향 대각선 방문 여부를 저장하는 딕셔너리
right_up_diagonal = {k: 0 for k in range(-n + 1, n)}


def count_possible_bishops(start_diagonal):
    """
    특정 대각선부터 탐색하여 앞으로 놓을 수 있는 비숍의 최대 개수를 계산하는 함수
    """
    count = 0
    for diagonal in range(start_diagonal, 2 * n - 1):
        for x in range(diagonal + 1):
            y = diagonal - x
            if (0 <= x < n) and (0 <= y < n) and board[x][y] and right_up_diagonal[x - y] == 0:
                count += 1
                break  # 해당 대각선에서 하나만 놓을 수 있으므로 더 탐색할 필요 없음
    return count


def backtrack(left_down_diagonal, placed_bishops):
    """
    백트래킹을 사용하여 비숍을 놓을 수 있는 최대 개수를 탐색하는 함수
    """
    global max_bishops

    # 모든 대각선을 탐색한 경우, 최대 비숍 개수 갱신
    if left_down_diagonal == 2 * n - 1:
        max_bishops = max(max_bishops, placed_bishops)
        return

    # 앞으로 놓을 수 있는 비숍 개수를 확인하여 가지치기 수행
    possible_bishops = count_possible_bishops(left_down_diagonal)
    if placed_bishops + possible_bishops <= max_bishops:
        return  # 더 탐색할 필요 없음

    # 현재 대각선에서 비숍을 놓을 수 있는 모든 위치 탐색
    for x in range(left_down_diagonal + 1):
        y = left_down_diagonal - x
        if (0 <= x < n) and (0 <= y < n) and board[x][y] and right_up_diagonal[x - y] == 0:
            # 비숍 배치
            right_up_diagonal[x - y] = 1
            backtrack(left_down_diagonal + 1, placed_bishops + 1)
            # 백트래킹 (비숍 배치를 원래대로 되돌리기)
            right_up_diagonal[x - y] = 0

    # 현재 대각선에서 비숍을 놓지 않는 경우도 고려
    backtrack(left_down_diagonal + 1, placed_bishops)


backtrack(0, 0)

print(max_bishops)