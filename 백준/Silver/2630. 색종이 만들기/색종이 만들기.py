import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
mat = [[int(num) for num in input().split()] for _ in range(N)]


def solution():
    white, blue = 0, 0

    def is_paper(i, j, n, flag) -> bool:
        color = 1 if flag == "blue" else 0

        for y in range(j, j + n):
            for x in range(i, i + n):
                if mat[y][x] != color:
                    return False

        return True

    def recur(x, y, n):
        nonlocal blue
        nonlocal white

        if n <= 1:
            if mat[y][x] == 1:
                blue += 1
            else:
                white += 1
            return

        if is_paper(x, y, n, "blue"):
            blue += 1
            return

        if is_paper(x, y, n, "white"):
            white += 1
            return

        half = n // 2

        recur(x, y, half)
        recur(x, y + half, half)
        recur(x + half, y, half)
        recur(x + half, y + half, half)

    recur(0, 0, N)

    print(white)
    print(blue)


solution()
