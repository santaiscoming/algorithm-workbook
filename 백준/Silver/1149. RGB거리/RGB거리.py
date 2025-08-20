import sys
import math

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]


def solve():
    dp = [[-1] * 3 for _ in range(n)]

    def _recur(depth, color):
        if depth == n:
            return 0

        if dp[depth][color] != -1:
            return dp[depth][color]

        best = math.inf
        for i, cost in enumerate(costs[depth]):
            if i != color:
                best = min(best, _recur(depth + 1, i) + cost)

        dp[depth][color] = best
        return best

    best = math.inf
    for i, cost in enumerate(costs[0]):
        best = min(best, _recur(1, i) + cost)

    print(best)


solve()
