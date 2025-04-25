import sys
from collections import deque
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(n)]


def solution():
    result = math.inf
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((0, 0, 1, 0))
    visited[0][0][0] = True

    while q:
        x, y, distance, isBroken = q.popleft()

        if (x, y) == (m - 1, n - 1):
            result = min(result, distance)
            continue

        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if mat[ny][nx] == 1:
                    if not isBroken and not visited[ny][nx][1]:
                        visited[ny][nx][1] = True
                        q.append((nx, ny, distance + 1, 1))
                elif mat[ny][nx] == 0:
                    if not visited[ny][nx][isBroken]:
                        visited[ny][nx][isBroken] = True
                        q.append((nx, ny, distance + 1, isBroken))

    print(result) if result != math.inf else print(-1)


solution()
