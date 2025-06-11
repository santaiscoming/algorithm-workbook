import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def checkTShape(x, y, acc):
        nonlocal result

        tShapes = [
            [(1, 0), (-1, 0), (0, -1)],
            [(1, 0), (0, -1), (0, 1)],
            [(-1, 0), (0, 1), (0, -1)],
            [(1, 0), (-1, 0), (0, 1)],
        ]

        for T_DIR in tShapes:
            isPossibleShape = True
            shapeValue = acc

            for dx, dy in T_DIR:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    shapeValue += mat[ny][nx]
                else:
                    isPossibleShape = False
                    break

            if isPossibleShape:
                result = max(result, shapeValue)

    def dfs(x, y, depth, acc):
        nonlocal result

        if depth == 4:
            result = max(result, acc)
            return

        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(nx, ny, depth + 1, acc + mat[ny][nx])
                visited[ny][nx] = False

    result = 0
    visited = [[False] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            visited[y][x] = True
            dfs(x, y, 1, mat[y][x])
            checkTShape(x, y, mat[y][x])
            visited[y][x] = False

    print(result)


solution()
