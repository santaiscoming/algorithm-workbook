import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

mat = [list(map(int, input().split())) for _ in range(9)]


def solution1():
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                empty_cells.append((i, j))

    # 각 행, 열, 박스에서 사용된 숫자들을 비트마스크로 관리
    row_used = [0] * 9
    col_used = [0] * 9
    box_used = [0] * 9

    # 초기 상태 설정
    for i in range(9):
        for j in range(9):
            if mat[i][j] != 0:
                num = mat[i][j]
                row_used[i] |= 1 << num
                col_used[j] |= 1 << num
                box_used[(i // 3) * 3 + (j // 3)] |= 1 << num

    def solve(idx):
        if idx == len(empty_cells):
            return True

        row, col = empty_cells[idx]
        box_idx = (row // 3) * 3 + (col // 3)

        for num in range(1, 10):
            bit = 1 << num
            if (
                not (row_used[row] & bit)
                and not (col_used[col] & bit)
                and not (box_used[box_idx] & bit)
            ):
                mat[row][col] = num
                row_used[row] |= bit
                col_used[col] |= bit
                box_used[box_idx] |= bit

                if solve(idx + 1):
                    return True

                mat[row][col] = 0
                row_used[row] &= ~bit
                col_used[col] &= ~bit
                box_used[box_idx] &= ~bit

        return False

    solve(0)

    for row in mat:
        print(*row)


solution1()


def solution():
    def findEmptyCell(mat):
        for y in range(9):
            for x in range(9):
                if mat[y][x] == 0:
                    return y, x
        return None, None

    def isSafe(x, y, num):
        if any((mat[y][i] == num) or (mat[i][x] == num) for i in range(9)):
            return False

        sx, sy = (x // 3) * 3, (y // 3) * 3
        if any(mat[sy + j][sx + i] == num for i in range(3) for j in range(3)):
            return False

        return True

    def solve():
        y, x = findEmptyCell(mat)
        if y is None:
            return True

        for num in range(1, 10):
            if isSafe(x, y, num):
                mat[y][x] = num
                if solve():
                    return True
        mat[y][x] = 0
        return False

    solve()

    for row in mat:
        print(*row)


# solution()


def slowSolution():
    def isSafe(x, y, num):
        if any((mat[y][i] == num) or (mat[i][x] == num) for i in range(9)):
            return False

        sx, sy = (x // 3) * 3, (y // 3) * 3
        if any(mat[sy + j][sx + i] == num for i in range(3) for j in range(3)):
            return False

        return True

    def dfs(pos):
        if pos == 81:
            return True

        y, x = pos // 9, pos % 9

        if mat[y][x] != 0:
            return dfs(pos + 1)

        for num in range(1, 10):
            if isSafe(x, y, num):
                mat[y][x] = num
                if dfs(pos + 1):
                    return True
                mat[y][x] = 0

        return False

    dfs(0)

    for row in mat:
        print(*row)


# slowSolution()
