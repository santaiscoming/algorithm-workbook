import sys
import math

sys.setrecursionlimit(10**5)
# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]


def solve():
    def _getMinCost(n, color, lastColor):
        if n < 0:
            return 0

        if dp[n][color] != -1:
            return dp[n][color]

        best = math.inf
        for i, cost in enumerate(costs[n]):
            if i == color:
                continue
            if n == 0 and i == lastColor:
                continue

            best = min(best, _getMinCost(n - 1, i, lastColor) + cost)

        dp[n][color] = best
        return best

    best = math.inf
    for lastColor, cost in enumerate(costs[n - 1]):
        dp = [[-1] * 3 for _ in range(n)]
        best = min(best, _getMinCost(n - 2, lastColor, lastColor) + cost)

    print(best)


solve()
