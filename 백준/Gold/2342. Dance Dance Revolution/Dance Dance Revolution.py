import sys
import math

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

arr = list(map(int, input().split()))


def solve():
    dist = {
        0: {i: 2 for i in range(5)},
        1: {
            1: 1,
            2: 3,
            3: 4,
            4: 3,
        },
        2: {
            1: 3,
            2: 1,
            3: 3,
            4: 4,
        },
        3: {
            1: 4,
            2: 3,
            3: 1,
            4: 3,
        },
        4: {
            1: 3,
            2: 4,
            3: 3,
            4: 1,
        },
    }

    def getMinDist(left, right, depth):
        if depth > 0 and left == right:
            return math.inf
        if depth == n - 1:
            return 0

        if dp[depth][left][right] != -1:
            return dp[depth][left][right]

        nextPos = arr[depth]
        best = math.inf
        best = min(
            best,
            getMinDist(left, nextPos, depth + 1) + dist[right][nextPos],
            getMinDist(nextPos, right, depth + 1) + dist[left][nextPos],
        )
        dp[depth][left][right] = best
        return best

    n = len(arr)
    dp = [[[-1] * 5 for _ in range(5)] for _ in range(n - 1)]
    result = getMinDist(0, 0, 0)
    print(result)


solve()
