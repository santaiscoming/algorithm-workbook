import sys
import math

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

c, n = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]


def solution():
    minCost = math.inf
    dp = [math.inf] * (c + 1)

    def dfs(cost, profit, start):
        nonlocal minCost

        if profit >= c:
            minCost = min(minCost, cost)
            return

        if dp[profit] <= cost:
            return

        dp[profit] = cost

        for i in range(start, n):
            curCost, curProfit = costs[i]

            dfs(cost + curCost, profit + curProfit, i)
            dfs(cost, profit, i + 1)

    dfs(0, 0, 0)
    print(minCost)


solution()
