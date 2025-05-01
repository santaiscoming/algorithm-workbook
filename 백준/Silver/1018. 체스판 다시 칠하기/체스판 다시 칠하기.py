import sys
import math


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]


def solution():
    WHITE = "W"
    BLACK = "B"

    def flipColor(curr):
        return WHITE if curr == BLACK else BLACK

    def repaintCount(x, y, mat, startColor):
        count = 0

        currColor = startColor
        for dy in range(8):
            for dx in range(8):
                nx, ny = x + dx, y + dy
                if currColor != mat[ny][nx]:
                    count += 1

                currColor = flipColor(currColor)
            currColor = flipColor(currColor)

        return count

    result = math.inf

    for y in range(n):
        for x in range(m):
            if x + 8 <= m and y + 8 <= n:
                result = min(
                    result,
                    repaintCount(x, y, mat, WHITE),
                    repaintCount(x, y, mat, BLACK),
                )

    print(result)


solution()
