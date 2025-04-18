import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def solution():
    mat = [[math.inf] * (n) for _ in range(n)]
    for i in range(n):
        mat[i][i] = 0
    for u, v in edges:
        mat[u - 1][v - 1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]

    result = 0
    for i in range(n):
        known = 0
        for j in range(n):
            if i == j:
                continue
            if mat[i][j] != math.inf or mat[j][i] != math.inf:
                known += 1

        if known >= n - 1:
            result += 1

    print(result)


solution()
