import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


N = int(input())
# k -> row, board[k] -> col (놓을 수 있는 위치)
board = [False] * N
board_right_up = [False] * (N * 2)
board_right_down = [False] * (N * 2)
count = 0


def queen(row):
    global count

    if row >= N:
        count += 1
        return

    for col in range(0, N):
        if (
            board[col]
            or board_right_up[row + col]
            or board_right_down[(row - col + N - 1)]
        ):
            continue
        board[col] = True
        board_right_up[row + col] = True
        board_right_down[row - col + N - 1] = True
        queen(row + 1)
        board[col] = False
        board_right_up[row + col] = False
        board_right_down[row - col + N - 1] = False


queen(0)
print(count)
