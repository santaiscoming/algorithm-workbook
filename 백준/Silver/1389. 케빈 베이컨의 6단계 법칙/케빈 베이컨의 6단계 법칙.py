import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def solution():
    dp = [[math.inf] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for s, v in edges:
        dp[s - 1][v - 1] = 1
        dp[v - 1][s - 1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    kevin_rate = [0] * n
    for i in range(n):
        for j in range(n):
            tmp = min(dp[i][j], dp[j][i])

            if tmp != math.inf:
                kevin_rate[i] += tmp

    print(kevin_rate.index(min(kevin_rate)) + 1)


solution()
