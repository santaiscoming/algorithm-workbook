import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

c, n = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]


def solution():
    dpSize = c + max(profit for _, profit in info) + 1
    dp = [math.inf] * dpSize
    dp[0] = 0

    for i in range(dpSize):
        for cost, profit in info:
            if i >= profit:
                dp[i] = min(dp[i], dp[i - profit] + cost)

    print(min(dp[c:]))


solution()

