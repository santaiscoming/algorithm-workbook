import sys
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(matrix, start, end, visited, result):
    q = deque()
    sy, sx = start
    ey, ex = end

    if visited[sy][sx]:
        return
    # 만약 end (ey, ex)에 만나면 result.append(1)

    q.append(start)

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if (
                ny < 0
                or nx < 0
                or ny >= N
                or nx >= M
                or visited[ny][nx]
                or matrix[ny][nx] == 0
            ):
                continue
            elif matrix[ny][nx] == 1:
                result.append(1)

            visited[ny][nx] = True
            matrix[ny][nx] = matrix[cur_y][cur_x] + 1

            q.append((ny, nx))


def solution(matrix, start, end):
    sy, sx = start
    ey, ex = end
    visited = [[False] * M for _ in range(N)]
    result = []

    bfs(matrix, start, end, visited, result)

    print(matrix[N - 1][M - 1])


solution(matrix, (0, 0), (N - 1, M - 1))
