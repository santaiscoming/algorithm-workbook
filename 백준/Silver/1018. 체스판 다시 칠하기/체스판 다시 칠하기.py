import sys
import math


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]


def solution():
    def paint(x, y, mat):
        startBlackCount = 0
        startWhiteCount = 0

        for dy in range(8):
            isBlackTurn = True if dy % 2 == 1 else False

            for dx in range(8):
                nx, ny = x + dx, y + dy

                if (isBlackTurn and mat[ny][nx] == "W") or (
                    not isBlackTurn and mat[ny][nx] == "B"
                ):
                    startBlackCount += 1

                isBlackTurn = not isBlackTurn

        for dy in range(8):
            isWhiteTurn = True if dy % 2 == 1 else False

            for dx in range(8):
                nx, ny = x + dx, y + dy

                if (isWhiteTurn and mat[ny][nx] == "B") or (
                    not isWhiteTurn and mat[ny][nx] == "W"
                ):
                    startWhiteCount += 1

                isWhiteTurn = not isWhiteTurn

        return min(startBlackCount, startWhiteCount)

    result = math.inf

    for y in range(n):
        for x in range(m):
            if x + 8 <= m and y + 8 <= n:
                cnt = paint(x, y, mat)
                result = min(result, cnt)

    print(result)


solution()
