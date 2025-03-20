import sys
import math

# sys.stdin = open("./input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    p = [0] + [mat[0][0]] + [m[1] for m in mat]
    dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 0

    for l in range(1, n + 1):
        for i in range(1, n + 1 - l):
            j = i + l
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (p[i] * p[k + 1] * p[j + 1])
                if cost < dp[i][j]:
                    dp[i][j] = cost

    print(dp[1][n])


solution()
