import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

sdoku = [list(map(int, input().rstrip())) for _ in range(9)]


def solve():
    def findEmptyCells():
        result = []

        for y in range(9):
            for x in range(9):
                if sdoku[y][x] == 0:
                    result.append((x, y))

        return result

    def createUsedBitMap():
        rowUsed = [0] * 9
        colUsed = [0] * 9
        boxUsed = [0] * 9

        for row in range(9):
            for col in range(9):
                usedNum = sdoku[row][col]
                if usedNum != 0:
                    bit = 1 << (usedNum - 1)
                    rowUsed[row] |= bit
                    colUsed[col] |= bit
                    by, bx = (row // 3) * 3, col // 3
                    boxUsed[by + bx] |= bit

        return rowUsed, colUsed, boxUsed

    def dfs(depth, cells):
        if depth == len(cells):
            for r in sdoku:
                print("".join(map(str, r)))
            sys.exit(0)

        col, row = cells[depth]
        boxPos = ((row // 3) * 3) + (col // 3)
        usedBit = rowUsed[row] | colUsed[col] | boxUsed[boxPos]

        for num in range(1, 10):
            mask = 1 << (num - 1)

            if not (usedBit & mask):
                rowUsed[row] |= mask
                colUsed[col] |= mask
                boxUsed[boxPos] |= mask
                sdoku[row][col] = num

                dfs(depth + 1, cells)

                rowUsed[row] ^= mask
                colUsed[col] ^= mask
                boxUsed[boxPos] ^= mask
                sdoku[row][col] = 0

    emptyCells = findEmptyCells()
    rowUsed, colUsed, boxUsed = createUsedBitMap()

    dfs(0, emptyCells)


solve()
