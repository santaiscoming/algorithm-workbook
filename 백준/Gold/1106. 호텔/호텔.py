import sys
import math

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

c, n = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]


def solution():
    memo = {}

    def recur(profit):
        if profit in memo:
            return memo[profit]

        if profit <= 0:
            return 0

        minCost = math.inf

        for cost, curProfit in costs:
            minCost = min(minCost, cost + recur(profit - curProfit))

        memo[profit] = minCost

        return minCost

    print(recur(c))


solution()
