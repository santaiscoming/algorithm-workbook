import sys
import math


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


def solution():
    dp = [math.inf] * (n + 1)
    dp[0] = 0

    for i in range(3, n + 1):
        dp[i] = min(dp[i], dp[i - 3] + 1, dp[i - 5] + 1)

    print(dp[-1]) if dp[-1] != math.inf else print(-1)


solution()
