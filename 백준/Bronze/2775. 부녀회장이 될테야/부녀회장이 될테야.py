import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())
tc = [[int(input()) for _ in range(2)] for _ in range(t)]


def solution():
    for k, n in tc:
        mat = [[i + 1 for i in range(n)] for _ in range(k + 1)]

        for y in range(1, k + 1):
            for x in range(1, n):
                mat[y][x] = mat[y - 1][x] + mat[y][x - 1]

        print(mat[k][n - 1])


solution()
