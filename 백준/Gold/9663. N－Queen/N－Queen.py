import sys


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())

visited_col = [False] * (N * 2)
visited_우상향 = [False] * (N * 2)
visited_우하향 = [False] * (N * 2)
count = 0


# n : 퀸을 놓은 곳 (0부터시작)
# current_col : x축 and 행
def queen(curr_row):
    global count

    # 현재 말을 놓으려는 곳이 N이 되면 0부터 시작해서 모두 놓은것
    if curr_row == N:
        count += 1
        return

    for y in range(0, N):
        # **continue** 조건
        # if (열에 퀸이 있거나 visited[y축])
        # if (우상향 대각이 있거나 visited[x + y]) -> 좌표가 같다
        # if (우하향 대각이 있으면 (y - x - n - 1 => 1차원 배열이기에 대각선 모두 같은 값을 보장해야함으로))
        if (
            visited_col[y]
            or visited_우상향[curr_row + y]
            or visited_우하향[(curr_row - y + N - 1)]
        ):
            continue
        visited_col[y] = True
        visited_우상향[curr_row + y] = True
        visited_우하향[curr_row - y + N - 1] = True
        queen(curr_row + 1)
        visited_col[y] = False
        visited_우상향[curr_row + y] = False
        visited_우하향[curr_row - y + N - 1] = False


queen(0)
print(count)
