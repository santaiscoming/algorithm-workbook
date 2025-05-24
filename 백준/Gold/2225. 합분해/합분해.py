import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, k = map(int, input().split())


def solution():
    MOD = 1_000_000_000
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for j in range(n + 1):
        dp[1][j] = 1

    for i in range(2, k + 1):
        for j in range(n + 1):
            for x in range(j + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % MOD

    print(dp[k][n])


solution()
