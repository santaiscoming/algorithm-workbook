from collections import deque
import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]


def solve():
    DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def allWellDone(tomatoes):
        for y in range(n):
            for x in range(m):
                if tomatoes[y][x] == 0:
                    return False

        return True

    if allWellDone(tomatoes):
        print(0)
        return

    days = 0
    q = deque()
    for y in range(n):
        for x in range(m):
            if tomatoes[y][x] == 1:
                q.append((x, y))

    while q:
        size = len(q)
        for _ in range(size):
            cx, cy = q.popleft()

            for dx, dy in DIRECTION:
                nx, ny = cx + dx, cy + dy

                if (0 <= nx < m) and (0 <= ny < n) and (tomatoes[ny][nx] == 0):
                    tomatoes[ny][nx] = 1
                    q.append((nx, ny))
        days += 1

    if allWellDone(tomatoes):
        print(days - 1)
    else:
        print(-1)


solve()
