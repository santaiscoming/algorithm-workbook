import sys
from collections import deque
import math


# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m, k = map(int, input().split())
village = [
    list(map(lambda x: int(x) if x.isdigit() else x, input().rstrip()))
    for _ in range(n)
]


def solve():
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    startArr = [(x, y) for x in range(m) for y in range(n) if village[y][x] == "S"]
    destArr = [(x, y) for x in range(m) for y in range(n) if village[y][x] == "H"]
    if not startArr or not destArr:
        print(-1)
        return

    [start] = startArr
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    result = math.inf

    q = deque()
    q.append((*start, 0, 0, 0))  # x, y, prevX, prevY, cost

    while q:
        x, y, px, py, cost = q.popleft()

        for i, v in enumerate(DIRECTIONS):
            dx, dy = v
            nx, ny = x + dx, y + dy

            if (
                not (0 <= nx < m and 0 <= ny < n)
                or village[ny][nx] == "X"
                or village[ny][nx] == "S"
                or (nx, ny) == (px, py)
            ):
                continue

            if village[ny][nx] == "H":
                print(cost + 1)
                return

            prevUnlucky = village[py][px] if isinstance(village[py][px], int) else 0
            currUnlucky = village[y][x] if village[y][x] != "S" else 0
            nextUnlucky = village[ny][nx]
            if (prevUnlucky + currUnlucky + nextUnlucky) > k:
                continue

            if not visited[ny][nx][i]:
                visited[ny][nx][i] = True
                q.append((nx, ny, x, y, cost + 1))

    print(result) if result != math.inf else print(-1)


solve()
