import sys
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
apart = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j, visited):
    count = 0
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (
                ny < 0
                or nx < 0
                or ny >= N
                or nx >= N
                or visited[ny][nx]
                or apart[ny][nx] == 0
            ):
                continue

            visited[ny][nx] = True
            queue.append((ny, nx))
            count += 1

    return count


def solution(apart, N):
    visited = [[False] * N for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N):
            #  방문하거나 1이면 안가도 됨
            if visited[i][j] or apart[i][j] == 0:
                continue

            else:
                result.append(bfs(i, j, visited))

    print(len(result))
    for cnt in sorted(result):
        print(cnt + 1)


solution(apart, N)
