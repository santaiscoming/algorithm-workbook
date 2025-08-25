import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))


def solve():
    def getMaxCost(n):
        if n == 0:
            return 0
        if n < 0:
            return -math.inf

        if dp[n] != -1:
            return dp[n]

        best = 0
        for i in range(len(costs)):
            cardCnt = i + 1
            best = max(best, getMaxCost(n - cardCnt) + costs[i])

        dp[n] = best
        return best

    dp = [-1] * (len(costs) + 1)
    result = getMaxCost(n)
    print(result)


solve()
