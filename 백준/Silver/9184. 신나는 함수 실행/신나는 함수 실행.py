import sys
from itertools import takewhile


# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline


inputs = list(
    takewhile(
        lambda arr: not all(i == -1 for i in arr),
        iter(lambda: list(map(int, input().split())), None),
    )
)


def solution():
    MAX_RANGE = 21
    dp = [[[0] * MAX_RANGE for _ in range(MAX_RANGE)] for _ in range(MAX_RANGE)]

    def w(a, b, c) -> str:
        if all(0 <= num <= 20 for num in [a, b, c]) and dp[a][b][c]:
            return dp[a][b][c]

        result = 0
        if any(num <= 0 for num in [a, b, c]):
            result = 1
        elif any(num > 20 for num in [a, b, c]):
            result = w(20, 20, 20)
        elif a < b < c:
            result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            result = (
                w(a - 1, b, c)
                + w(a - 1, b - 1, c)
                + w(a - 1, b, c - 1)
                - w(a - 1, b - 1, c - 1)
            )

        if all(0 <= num <= 20 for num in [a, b, c]):
            dp[a][b][c] = result

        return result

    for a, b, c in inputs:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")


solution()
