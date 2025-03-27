import sys
import math

# sys.stdin = open("./input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
smalls = [int(input()) for _ in range(m)]


def solution():
    small_stones = set(smalls)
    max_speed = int(math.sqrt(2 * n)) + 2
    dp = [[math.inf] * max_speed for _ in range(n + 1)]
    dp[1][0] = 0

    for pos in range(2, n + 1):
        if pos in small_stones:
            continue

        for speed in range(1, int(math.sqrt(2 * pos)) + 1):
            dp[pos][speed] = (
                min(
                    dp[pos - speed][speed + 1],
                    dp[pos - speed][speed],
                    dp[pos - speed][speed - 1],
                )
                + 1
            )

    result = min(dp[n])
    if result == math.inf:
        print(-1)
    else:
        print(result)


solution()
